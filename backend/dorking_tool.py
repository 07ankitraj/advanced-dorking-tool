"""
Advanced Google Dorking Tool
Provides powerful search capabilities using advanced search operators
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import requests
from bs4 import BeautifulSoup
import urllib.parse
import time
import json
from utils import (
    add_to_history, get_history, clear_history,
    add_favorite, get_favorites, remove_favorite,
    get_statistics,
    generate_subdomain_dork, generate_file_dork,
    generate_login_dork, generate_error_dork,
    generate_backup_dork, generate_config_dork
)

app = FastAPI(title="Advanced Dorking Tool")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class DorkQuery(BaseModel):
    query: str
    engine: str = "google"  # google, bing, duckduckgo
    num_results: int = 10


class CustomDork(BaseModel):
    site: Optional[str] = None
    filetype: Optional[str] = None
    inurl: Optional[str] = None
    intitle: Optional[str] = None
    intext: Optional[str] = None
    ext: Optional[str] = None
    link: Optional[str] = None
    related: Optional[str] = None
    cache: Optional[str] = None
    allintitle: Optional[str] = None
    allinurl: Optional[str] = None
    allintext: Optional[str] = None


# Predefined dork templates
DORK_TEMPLATES = {
    "sql_injection": [
        'inurl:".php?id=" intext:"SQL syntax"',
        'inurl:".php?catid=" intext:"MySQL"',
        'inurl:"index.php?id=" site:*',
        'inurl:"product.php?id="',
        'inurl:"news.php?id="',
    ],
    "exposed_files": [
        'filetype:sql intext:password',
        'filetype:log intext:password',
        'filetype:env "DB_PASSWORD"',
        'filetype:config intext:password',
        'filetype:txt intext:"username" intext:"password"',
    ],
    "admin_panels": [
        'inurl:admin intitle:login',
        'inurl:administrator intitle:login',
        'inurl:"admin/login.php"',
        'inurl:"admin/admin.php"',
        'inurl:wp-admin',
    ],
    "exposed_cameras": [
        'inurl:"view.shtml" intitle:"Network Camera"',
        'inurl:"/view/index.shtml"',
        'inurl:"ViewerFrame?Mode="',
        'inurl:"MultiCameraFrame?Mode="',
        'intitle:"webcamXP 5"',
    ],
    "sensitive_directories": [
        'intitle:"Index of" +".ssh"',
        'intitle:"Index of" +".git"',
        'intitle:"Index of" +"backup"',
        'intitle:"Index of" +"config"',
        'intitle:"Index of" +"database"',
    ],
    "exposed_documents": [
        'filetype:pdf "confidential"',
        'filetype:doc "confidential"',
        'filetype:xls "confidential"',
        'filetype:pdf inurl:resume',
        'filetype:docx "curriculum vitae"',
    ],
    "login_pages": [
        'intitle:"login" inurl:"login.php"',
        'intitle:"admin login" inurl:"admin"',
        'inurl:"/login" intitle:"please login"',
        'inurl:"signup" | inurl:"register"',
    ],
    "error_messages": [
        'intitle:"error occurred" "server error"',
        'intext:"Warning: mysql_connect()"',
        'intext:"Warning: include()"',
        'intitle:"PHP Parse error"',
    ],
}


def build_dork_query(custom: CustomDork) -> str:
    """Build a dork query from custom parameters"""
    parts = []

    if custom.site:
        parts.append(f"site:{custom.site}")
    if custom.filetype:
        parts.append(f"filetype:{custom.filetype}")
    if custom.inurl:
        parts.append(f"inurl:{custom.inurl}")
    if custom.intitle:
        parts.append(f"intitle:{custom.intitle}")
    if custom.intext:
        parts.append(f"intext:{custom.intext}")
    if custom.ext:
        parts.append(f"ext:{custom.ext}")
    if custom.link:
        parts.append(f"link:{custom.link}")
    if custom.related:
        parts.append(f"related:{custom.related}")
    if custom.cache:
        parts.append(f"cache:{custom.cache}")
    if custom.allintitle:
        parts.append(f"allintitle:{custom.allintitle}")
    if custom.allinurl:
        parts.append(f"allinurl:{custom.allinurl}")
    if custom.allintext:
        parts.append(f"allintext:{custom.allintext}")

    return " ".join(parts)


def search_google(query: str, num_results: int = 10):
    """Search Google with dork query"""
    results = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }

    encoded_query = urllib.parse.quote_plus(query)
    url = f"https://www.google.com/search?q={encoded_query}&num={num_results}&hl=en"

    try:
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Try multiple selectors for different Google layouts
        search_results = soup.find_all('div', class_='g') or soup.find_all(
            'div', {'data-sokoban-container': True})

        if not search_results:
            # Fallback: try finding any div with h3 inside
            search_results = soup.find_all('div', recursive=True)
            search_results = [div for div in search_results if div.find('h3')]

        for result in search_results[:num_results]:
            # Try multiple ways to find title
            title_elem = result.find('h3') or result.find('h2')
            # Find the first <a> tag
            link_elem = result.find('a', href=True)
            # Try to find snippet
            snippet_elem = result.find(
                'div', class_=['VwiC3b', 'yXK7lf', 'IsZvec']) or result.find('span')

            if title_elem and link_elem:
                title = title_elem.get_text(strip=True)
                link = link_elem.get('href', '')

                # Clean up the URL if it's a Google redirect
                if link.startswith('/url?q='):
                    link = link.split('/url?q=')[1].split('&')[0]

                snippet = snippet_elem.get_text(
                    strip=True) if snippet_elem else "No description available"

                # Only add if we have a valid external URL
                if link.startswith('http'):
                    results.append({
                        'title': title,
                        'url': link,
                        'snippet': snippet
                    })

        # If no results found, return dummy data for testing
        if not results:
            results.append({
                'title': f'Test Result for: {query}',
                'url': 'https://www.google.com',
                'snippet': 'No results found from Google. This may be due to rate limiting or CAPTCHA. Try using DuckDuckGo or Bing instead.'
            })

        return results
    except Exception as e:
        # Return error as a result instead of raising exception
        return [{
            'title': 'Search Error',
            'url': 'https://www.google.com',
            'snippet': f'Error performing search: {str(e)}. Try a different search engine or check your internet connection.'
        }]


def search_bing(query: str, num_results: int = 10):
    """Search Bing with dork query"""
    results = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    encoded_query = urllib.parse.quote_plus(query)
    url = f"https://www.bing.com/search?q={encoded_query}&count={num_results}"

    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        search_results = soup.find_all('li', class_='b_algo')

        for result in search_results[:num_results]:
            title_elem = result.find('h2')
            link_elem = result.find('a')
            snippet_elem = result.find('p')

            if title_elem and link_elem:
                title = title_elem.get_text()
                link = link_elem.get('href', '')
                snippet = snippet_elem.get_text() if snippet_elem else ""

                results.append({
                    'title': title,
                    'url': link,
                    'snippet': snippet
                })

        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")


def search_duckduckgo(query: str, num_results: int = 10):
    """Search DuckDuckGo with dork query"""
    results = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    encoded_query = urllib.parse.quote_plus(query)
    url = f"https://html.duckduckgo.com/html/?q={encoded_query}"

    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        search_results = soup.find_all('div', class_='result')

        for result in search_results[:num_results]:
            title_elem = result.find('a', class_='result__a')
            snippet_elem = result.find('a', class_='result__snippet')

            if title_elem:
                title = title_elem.get_text()
                link = title_elem.get('href', '')
                snippet = snippet_elem.get_text() if snippet_elem else ""

                results.append({
                    'title': title,
                    'url': link,
                    'snippet': snippet
                })

        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")


@app.get("/")
def read_root():
    return {
        "message": "Advanced Dorking Tool API",
        "version": "1.0",
        "endpoints": ["/search", "/templates", "/build-dork"]
    }


@app.get("/templates")
def get_templates():
    """Get all predefined dork templates"""
    return {
        "categories": list(DORK_TEMPLATES.keys()),
        "templates": DORK_TEMPLATES
    }


@app.get("/templates/{category}")
def get_category_templates(category: str):
    """Get dork templates for a specific category"""
    if category not in DORK_TEMPLATES:
        raise HTTPException(status_code=404, detail="Category not found")
    return {
        "category": category,
        "dorks": DORK_TEMPLATES[category]
    }


@app.post("/search")
def search(dork: DorkQuery):
    """Execute a dork query"""
    try:
        if dork.engine == "google":
            results = search_google(dork.query, dork.num_results)
        elif dork.engine == "bing":
            results = search_bing(dork.query, dork.num_results)
        elif dork.engine == "duckduckgo":
            results = search_duckduckgo(dork.query, dork.num_results)
        else:
            raise HTTPException(
                status_code=400, detail="Invalid search engine")

        # Add to history
        add_to_history(dork.query, dork.engine, len(results))

        return {
            "query": dork.query,
            "engine": dork.engine,
            "results": results,
            "total": len(results)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/build-dork")
def build_dork(custom: CustomDork):
    """Build a custom dork query from parameters"""
    query = build_dork_query(custom)
    return {
        "query": query,
        "message": "Custom dork query built successfully"
    }


@app.get("/operators")
def get_operators():
    """Get list of available dork operators"""
    return {
        "operators": [
            {
                "name": "site:",
                "description": "Search within a specific site or domain",
                "example": "site:example.com"
            },
            {
                "name": "filetype:",
                "description": "Search for specific file types",
                "example": "filetype:pdf"
            },
            {
                "name": "inurl:",
                "description": "Search for pages with specific terms in URL",
                "example": "inurl:admin"
            },
            {
                "name": "intitle:",
                "description": "Search for pages with specific terms in title",
                "example": "intitle:login"
            },
            {
                "name": "intext:",
                "description": "Search for pages with specific terms in body text",
                "example": "intext:password"
            },
            {
                "name": "cache:",
                "description": "View Google's cached version of a page",
                "example": "cache:example.com"
            },
            {
                "name": "link:",
                "description": "Find pages that link to a specific URL",
                "example": "link:example.com"
            },
            {
                "name": "related:",
                "description": "Find sites related to a given domain",
                "example": "related:example.com"
            },
            {
                "name": "allintitle:",
                "description": "Search for pages with all terms in title",
                "example": "allintitle:admin login"
            },
            {
                "name": "allinurl:",
                "description": "Search for pages with all terms in URL",
                "example": "allinurl:admin login"
            },
            {
                "name": "allintext:",
                "description": "Search for pages with all terms in body",
                "example": "allintext:username password"
            }
        ]
    }

# History and favorites endpoints


@app.get("/history")
def get_search_history(limit: int = 50):
    """Get search history"""
    return {"history": get_history(limit)}


@app.delete("/history")
def delete_history():
    """Clear search history"""
    clear_history()
    return {"message": "History cleared successfully"}


@app.get("/favorites")
def get_favorite_queries():
    """Get favorite queries"""
    return {"favorites": get_favorites()}


@app.post("/favorites")
def add_favorite_query(name: str, query: str, category: str = "Custom"):
    """Add a query to favorites"""
    favorite = add_favorite(query, name, category)
    return {"message": "Added to favorites", "favorite": favorite}


@app.delete("/favorites/{index}")
def delete_favorite(index: int):
    """Remove a favorite query"""
    removed = remove_favorite(index)
    if removed:
        return {"message": "Removed from favorites", "removed": removed}
    raise HTTPException(status_code=404, detail="Favorite not found")


@app.get("/statistics")
def get_stats():
    """Get usage statistics"""
    return {"statistics": get_statistics()}

# Advanced dork generators


class DomainDork(BaseModel):
    domain: str


class FileDork(BaseModel):
    domain: str
    filetypes: List[str]


@app.post("/generate/subdomain")
def generate_subdomain_query(data: DomainDork):
    """Generate dork to find subdomains"""
    query = generate_subdomain_dork(data.domain)
    return {"query": query, "description": "Find subdomains"}


@app.post("/generate/files")
def generate_files_query(data: FileDork):
    """Generate dork to find specific files"""
    query = generate_file_dork(data.domain, data.filetypes)
    return {"query": query, "description": "Find specific file types"}


@app.post("/generate/login")
def generate_login_query(data: DomainDork):
    """Generate dork to find login pages"""
    query = generate_login_dork(data.domain)
    return {"query": query, "description": "Find login pages"}


@app.post("/generate/error")
def generate_error_query(data: DomainDork):
    """Generate dork to find error pages"""
    query = generate_error_dork(data.domain)
    return {"query": query, "description": "Find error pages"}


@app.post("/generate/backup")
def generate_backup_query(data: DomainDork):
    """Generate dork to find backup files"""
    query = generate_backup_dork(data.domain)
    return {"query": query, "description": "Find backup files"}


@app.post("/generate/config")
def generate_config_query(data: DomainDork):
    """Generate dork to find configuration files"""
    query = generate_config_dork(data.domain)
    return {"query": query, "description": "Find configuration files"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
