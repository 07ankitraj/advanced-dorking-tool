# 🎯 Advanced Dorking Tool - Complete Usage Guide

## Table of Contents
1. [Getting Started](#getting-started)
2. [Basic Search](#basic-search)
3. [Using Templates](#using-templates)
4. [Building Custom Dorks](#building-custom-dorks)
5. [Advanced Techniques](#advanced-techniques)
6. [Real-World Examples](#real-world-examples)
7. [Best Practices](#best-practices)
8. [Troubleshooting](#troubleshooting)

## Getting Started

### Quick Start
1. Open two terminals/command prompts
2. Terminal 1: Start the backend
   ```bash
   cd backend
   python dorking_tool.py
   ```
3. Terminal 2: Start the frontend
   ```bash
   cd frontend
   npm run dev
   ```
4. Open your browser to `http://localhost:5173`

### Alternative: Use the startup script
Simply run: `.\start.ps1` (Windows PowerShell)

## Basic Search

### Simple Query
1. Go to the "Search" tab
2. Enter your query: `site:example.com`
3. Select search engine (Google/Bing/DuckDuckGo)
4. Click "Search"

### Query Syntax
- Use quotes for exact phrases: `"admin login"`
- Use OR for alternatives: `login | signin`
- Use minus to exclude: `site:example.com -www`
- Use parentheses to group: `(admin | login) password`

## Using Templates

The tool includes 8 pre-built template categories:

### 1. SQL Injection
Find potential SQL injection vulnerabilities
- Click on "Templates" tab
- Select "SQL Injection" category
- Click any dork to use it

Example dorks:
- `inurl:".php?id=" intext:"SQL syntax"`
- `inurl:"product.php?id="`

### 2. Exposed Files
Discover sensitive files
- Configuration files: `.env`, `.config`
- Database dumps: `.sql`
- Log files: `.log`

### 3. Admin Panels
Locate administration interfaces
- WordPress admin panels
- Custom admin pages
- Dashboard logins

### 4. Exposed Cameras
Find publicly accessible webcams
- Network cameras
- IP cameras
- Surveillance systems

### 5. Sensitive Directories
Discover exposed directories
- `.git` repositories
- `.ssh` directories
- Backup folders

### 6. Exposed Documents
Find confidential documents
- PDFs marked "confidential"
- Resume/CV files
- Internal documents

### 7. Login Pages
Locate authentication pages
- Login forms
- Registration pages
- Sign-in portals

### 8. Error Messages
Find pages with error information
- PHP errors
- MySQL errors
- Stack traces

## Building Custom Dorks

### Using the Dork Builder
1. Go to "Dork Builder" tab
2. Fill in the form fields:
   - **Site**: Target domain (e.g., `example.com`)
   - **File Type**: Specific file extensions (e.g., `pdf`)
   - **In URL**: Terms in the URL (e.g., `admin`)
   - **In Title**: Terms in page title (e.g., `login`)
   - **In Text**: Terms in page content (e.g., `password`)
3. Click "Build Dork Query"
4. Review the generated query
5. Click "Search with This Query"

### Field Combinations
You can combine multiple fields for powerful queries:

**Example 1: Find PDFs on a domain**
- Site: `example.com`
- File Type: `pdf`
Result: `site:example.com filetype:pdf`

**Example 2: Find admin login pages**
- Site: `example.com`
- In URL: `admin`
- In Title: `login`
Result: `site:example.com inurl:admin intitle:login`

**Example 3: Find configuration files**
- Site: `example.com`
- File Type: `env`
- In Text: `DB_PASSWORD`
Result: `site:example.com filetype:env intext:DB_PASSWORD`

## Advanced Techniques

### 1. Subdomain Discovery
Find all subdomains of a domain:
```
site:*.example.com -site:www.example.com
```

### 2. Technology Detection
Find sites using specific technologies:
```
intext:"Powered by WordPress" site:*.com
intext:"built with React"
```

### 3. Sensitive Parameter Detection
Find URLs with potentially vulnerable parameters:
```
site:example.com inurl:id= | inurl:page= | inurl:cat=
```

### 4. Directory Listing
Find open directory listings:
```
intitle:"Index of" site:example.com
intitle:"directory listing" site:example.com
```

### 5. Email Harvesting
Find email addresses on a domain:
```
site:example.com intext:"@example.com"
```

### 6. Document Discovery
Find specific document types:
```
site:example.com (filetype:pdf | filetype:doc | filetype:xls)
```

### 7. Cache Exploration
View cached versions of pages:
```
cache:example.com/important-page
```

### 8. Related Site Discovery
Find sites related to a domain:
```
related:example.com
```

## Real-World Examples

### Example 1: Security Audit
**Goal**: Find potential security issues on your own website

1. Find exposed configuration files:
   ```
   site:yoursite.com filetype:env
   site:yoursite.com inurl:config
   ```

2. Find backup files:
   ```
   site:yoursite.com (filetype:bak | filetype:backup | filetype:old)
   ```

3. Find error pages:
   ```
   site:yoursite.com intitle:"error" | intitle:"warning"
   ```

### Example 2: Competitive Intelligence
**Goal**: Research competitor's technology stack

1. Find technology mentions:
   ```
   site:competitor.com intext:"powered by"
   site:competitor.com intext:"built with"
   ```

2. Find job postings:
   ```
   site:competitor.com inurl:careers | inurl:jobs
   ```

3. Find documentation:
   ```
   site:competitor.com (inurl:docs | inurl:api | inurl:developer)
   ```

### Example 3: OSINT Investigation
**Goal**: Gather public information about a domain

1. Find social media profiles:
   ```
   site:twitter.com "example.com"
   site:linkedin.com "example.com"
   ```

2. Find news mentions:
   ```
   "example.com" site:news.google.com
   ```

3. Find archived content:
   ```
   site:web.archive.org example.com
   ```

### Example 4: Content Discovery
**Goal**: Find specific content across the web

1. Find research papers:
   ```
   filetype:pdf "machine learning" "neural networks"
   ```

2. Find presentations:
   ```
   filetype:ppt | filetype:pptx "artificial intelligence"
   ```

3. Find datasets:
   ```
   filetype:csv | filetype:json "dataset" | "data"
   ```

## Best Practices

### 1. Start Broad, Then Narrow
- Begin with general queries
- Refine based on initial results
- Add more specific operators gradually

### 2. Use Multiple Search Engines
- Google: Most comprehensive
- Bing: Different indexing
- DuckDuckGo: Privacy-focused, different results

### 3. Combine Operators Effectively
```
Good: site:example.com filetype:pdf intext:"confidential"
Better: site:example.com (filetype:pdf | filetype:doc) (intext:"confidential" | intext:"internal")
```

### 4. Respect Rate Limits
- Don't make too many requests too quickly
- Use different search engines if blocked
- Wait between searches if necessary

### 5. Verify Results
- Always verify findings manually
- Don't rely solely on automated results
- Context matters

### 6. Document Your Findings
- Use the export feature
- Keep track of effective queries
- Build your own template library

### 7. Stay Ethical
- Only search for public information
- Don't access unauthorized resources
- Respect privacy and laws
- Get permission for security testing

## Troubleshooting

### Problem: No Results Found
**Solutions:**
- Try different search engines
- Simplify your query
- Check if the domain is indexed
- Remove restrictive operators

### Problem: Search Engine Blocking
**Solutions:**
- Wait before searching again
- Use a different search engine
- Reduce search frequency
- Use a VPN if necessary

### Problem: Results Not Relevant
**Solutions:**
- Add more specific operators
- Use exact phrase matching with quotes
- Exclude unwanted terms with minus
- Try different operator combinations

### Problem: Backend Not Responding
**Solutions:**
- Check if backend is running on port 8000
- Restart the backend server
- Check firewall settings
- Verify Python dependencies are installed

### Problem: Frontend Not Loading
**Solutions:**
- Check if frontend is running on port 5173
- Clear browser cache
- Check browser console for errors
- Restart the development server

## Advanced Query Patterns

### Pattern 1: Multiple File Types
```
site:example.com (filetype:pdf | filetype:doc | filetype:xls | filetype:ppt)
```

### Pattern 2: Date Ranges
```
site:example.com "report" 2020..2024
```

### Pattern 3: Wildcard Domains
```
site:*.example.com
```

### Pattern 4: Excluding Common Pages
```
site:example.com -inurl:index -inurl:home -inurl:about
```

### Pattern 5: Complex Boolean Logic
```
site:example.com ((admin | administrator) AND (login | signin)) -test
```

## Export and Analysis

### Exporting Results
1. Perform your search
2. Click "Export Results" button
3. Results saved as JSON file
4. Use for further analysis

### Analyzing Exported Data
The JSON file contains:
- URL of each result
- Page title
- Snippet/description
- Timestamp

You can process this with:
- Python scripts
- Excel/Spreadsheet software
- Data analysis tools
- Custom parsers

## Tips and Tricks

1. **Save Effective Queries**: Keep a list of queries that work well
2. **Use Favorites**: Save your best queries for quick access
3. **Check History**: Review past searches to avoid duplicates
4. **Batch Processing**: Run multiple related queries
5. **Screenshot Evidence**: Capture results for documentation
6. **Cross-Reference**: Verify findings across multiple sources
7. **Regular Updates**: Search engines update indexes regularly
8. **Custom Scripts**: Automate repetitive tasks with the API

## API Usage

The tool provides a REST API at `http://localhost:8000`

### Key Endpoints:
- `GET /templates` - Get all templates
- `POST /search` - Execute a search
- `POST /build-dork` - Build custom dork
- `GET /operators` - Get operator list
- `GET /history` - Get search history
- `GET /statistics` - Get usage stats

### Example API Call:
```bash
curl -X POST "http://localhost:8000/search" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "site:example.com filetype:pdf",
    "engine": "google",
    "num_results": 10
  }'
```

## Conclusion

This dorking tool is powerful and versatile. Use it responsibly:
- ✅ Security research (with permission)
- ✅ OSINT investigations
- ✅ Content discovery
- ✅ Competitive analysis
- ❌ Unauthorized access
- ❌ Privacy violations
- ❌ Illegal activities

Always follow the law and ethical guidelines!

---

**Remember**: Information is power. Use it wisely and responsibly.

Happy dorking! 🔍🎯
