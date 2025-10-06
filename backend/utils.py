"""
Additional utilities for the dorking tool
Includes query history, favorites, and advanced features
"""

import json
import os
from datetime import datetime
from typing import List, Dict

HISTORY_FILE = "query_history.json"
FAVORITES_FILE = "favorites.json"


def load_json_file(filename: str) -> List[Dict]:
    """Load data from JSON file"""
    if os.path.exists(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    return []


def save_json_file(filename: str, data: List[Dict]):
    """Save data to JSON file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def add_to_history(query: str, engine: str, results_count: int):
    """Add a query to search history"""
    history = load_json_file(HISTORY_FILE)

    entry = {
        "query": query,
        "engine": engine,
        "results_count": results_count,
        "timestamp": datetime.now().isoformat()
    }

    # Add to beginning of list and limit to 100 entries
    history.insert(0, entry)
    history = history[:100]

    save_json_file(HISTORY_FILE, history)
    return entry


def get_history(limit: int = 50) -> List[Dict]:
    """Get search history"""
    history = load_json_file(HISTORY_FILE)
    return history[:limit]


def clear_history():
    """Clear all search history"""
    save_json_file(HISTORY_FILE, [])


def add_favorite(query: str, name: str, category: str = "Custom"):
    """Add a query to favorites"""
    favorites = load_json_file(FAVORITES_FILE)

    entry = {
        "name": name,
        "query": query,
        "category": category,
        "added_at": datetime.now().isoformat()
    }

    favorites.append(entry)
    save_json_file(FAVORITES_FILE, favorites)
    return entry


def get_favorites() -> List[Dict]:
    """Get all favorite queries"""
    return load_json_file(FAVORITES_FILE)


def remove_favorite(index: int):
    """Remove a favorite by index"""
    favorites = load_json_file(FAVORITES_FILE)
    if 0 <= index < len(favorites):
        removed = favorites.pop(index)
        save_json_file(FAVORITES_FILE, favorites)
        return removed
    return None


def get_statistics():
    """Get usage statistics"""
    history = load_json_file(HISTORY_FILE)

    if not history:
        return {
            "total_searches": 0,
            "total_results": 0,
            "most_used_engine": None,
            "recent_searches": 0
        }

    # Calculate statistics
    total_searches = len(history)
    total_results = sum(h.get('results_count', 0) for h in history)

    # Count engines
    engines = {}
    for h in history:
        engine = h.get('engine', 'unknown')
        engines[engine] = engines.get(engine, 0) + 1

    most_used_engine = max(engines.items(), key=lambda x: x[1])[
        0] if engines else None

    # Recent searches (last 24 hours)
    now = datetime.now()
    recent_searches = 0
    for h in history:
        try:
            timestamp = datetime.fromisoformat(h['timestamp'])
            if (now - timestamp).days < 1:
                recent_searches += 1
        except:
            pass

    return {
        "total_searches": total_searches,
        "total_results": total_results,
        "most_used_engine": most_used_engine,
        "recent_searches": recent_searches,
        "engine_usage": engines
    }

# Advanced dork generators


def generate_subdomain_dork(domain: str) -> str:
    """Generate dork to find subdomains"""
    return f"site:*.{domain} -site:www.{domain}"


def generate_file_dork(domain: str, filetypes: List[str]) -> str:
    """Generate dork to find specific files on a domain"""
    types = " | ".join([f"filetype:{ft}" for ft in filetypes])
    return f"site:{domain} ({types})"


def generate_login_dork(domain: str) -> str:
    """Generate dork to find login pages"""
    return f'site:{domain} (inurl:login | inurl:signin | inurl:admin | intitle:"login" | intitle:"sign in")'


def generate_error_dork(domain: str) -> str:
    """Generate dork to find error pages"""
    return f'site:{domain} (intitle:"error" | intitle:"warning" | intext:"SQL syntax" | intext:"fatal error")'


def generate_backup_dork(domain: str) -> str:
    """Generate dork to find backup files"""
    return f'site:{domain} (filetype:sql | filetype:bak | filetype:backup | filetype:old | inurl:backup)'


def generate_config_dork(domain: str) -> str:
    """Generate dork to find configuration files"""
    return f'site:{domain} (filetype:env | filetype:config | filetype:ini | filetype:yaml | filetype:yml | inurl:config)'
