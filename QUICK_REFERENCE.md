# 🔍 Google Dork Operators - Quick Reference Card

## Basic Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `site:` | Search within specific domain | `site:example.com` |
| `filetype:` | Search for specific file types | `filetype:pdf` |
| `ext:` | Alternative for filetype | `ext:doc` |
| `inurl:` | Search in URL | `inurl:admin` |
| `intitle:` | Search in page title | `intitle:login` |
| `intext:` | Search in page content | `intext:password` |
| `cache:` | View cached version | `cache:example.com` |
| `link:` | Find pages linking to URL | `link:example.com` |
| `related:` | Find related websites | `related:example.com` |

## Advanced Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `allintitle:` | All terms in title | `allintitle:admin login` |
| `allinurl:` | All terms in URL | `allinurl:admin login` |
| `allintext:` | All terms in content | `allintext:username password` |
| `OR` | Either term (use pipe) | `admin OR login` |
| `-` | Exclude term | `-inurl:www` |
| `*` | Wildcard | `site:*.example.com` |
| `..` | Number range | `2020..2024` |
| `" "` | Exact phrase | `"admin panel"` |
| `( )` | Group terms | `(admin | login)` |

## Common Patterns

### Finding Login Pages
```
site:example.com (inurl:login | inurl:signin | intitle:"login")
```

### Finding Admin Panels
```
site:example.com (inurl:admin | intitle:"admin panel" | inurl:administrator)
```

### Finding Exposed Files
```
site:example.com (filetype:sql | filetype:env | filetype:config | filetype:log)
```

### Finding Subdomains
```
site:*.example.com -site:www.example.com
```

### Finding Backup Files
```
site:example.com (filetype:bak | filetype:backup | filetype:old | inurl:backup)
```

### Finding Configuration Files
```
site:example.com (filetype:env | filetype:config | filetype:ini | filetype:yaml)
```

### Finding Error Pages
```
site:example.com (intitle:"error" | intitle:"warning" | intext:"SQL syntax")
```

### Finding Documents
```
site:example.com (filetype:pdf | filetype:doc | filetype:xls | filetype:ppt)
```

### Finding Cameras
```
inurl:"view.shtml" intitle:"Network Camera"
```

### Finding Directory Listings
```
intitle:"Index of" site:example.com
```

## File Type Extensions

### Documents
- `pdf` - PDF documents
- `doc` / `docx` - Word documents
- `xls` / `xlsx` - Excel spreadsheets
- `ppt` / `pptx` - PowerPoint presentations
- `txt` - Text files

### Code & Config
- `php` - PHP files
- `asp` / `aspx` - ASP files
- `jsp` - Java Server Pages
- `env` - Environment files
- `config` - Configuration files
- `ini` - INI files
- `yaml` / `yml` - YAML files
- `json` - JSON files
- `xml` - XML files

### Database & Backup
- `sql` - SQL files
- `db` - Database files
- `bak` - Backup files
- `backup` - Backup files
- `old` - Old files

### Logs
- `log` - Log files
- `logs` - Log files

## Combination Examples

### Security Audit
```
site:yoursite.com (filetype:env | filetype:config | filetype:sql | filetype:bak)
```

### Finding Vulnerable Parameters
```
site:example.com (inurl:id= | inurl:page= | inurl:cat= | inurl:user=)
```

### Finding Sensitive Info
```
site:example.com (intext:password | intext:"db_password" | intext:"api_key")
```

### Finding Upload Directories
```
site:example.com (inurl:upload | inurl:uploads | intitle:"index of" upload)
```

### Finding Test/Dev Environments
```
site:example.com (inurl:test | inurl:dev | inurl:staging | inurl:beta)
```

### Finding Database Errors
```
site:example.com (intext:"mysql_connect" | intext:"Warning: mysql" | intext:"SQL syntax")
```

### Finding Admin Logins
```
inurl:admin intitle:login
```

### Finding Exposed Git Repositories
```
intitle:"Index of" .git
```

### Finding Exposed SSH Keys
```
intitle:"Index of" .ssh
```

### Finding PHP Info Pages
```
inurl:phpinfo.php
```

## Boolean Logic

### AND (implicit)
```
site:example.com admin login
```
(Both "admin" AND "login" must appear)

### OR (explicit)
```
site:example.com (admin | login)
```
(Either "admin" OR "login" must appear)

### NOT (exclusion)
```
site:example.com admin -test
```
(Include "admin" but exclude "test")

### Complex Logic
```
site:example.com ((admin | administrator) AND (login | signin)) -test
```

## Tips & Tricks

### 1. Start Simple, Add Complexity
```
Start: site:example.com
Add: site:example.com admin
Add: site:example.com inurl:admin intitle:login
```

### 2. Use Wildcards for Variations
```
site:*.example.com
inurl:login*
```

### 3. Combine Multiple File Types
```
site:example.com (filetype:pdf | filetype:doc | filetype:xls)
```

### 4. Search Multiple Domains
```
(site:example.com | site:example.org) admin
```

### 5. Exclude Common Pages
```
site:example.com -inurl:index -inurl:home -inurl:contact
```

### 6. Find Recently Indexed
Use date range (Google only):
```
site:example.com after:2024-01-01
```

### 7. Search in Specific Languages
```
site:example.com inlang:en
```

## Popular Dork Categories

### 🔐 Security Testing
- SQL injection points
- XSS vulnerable parameters  
- Open redirects
- Admin panels
- Exposed credentials

### 📁 File Discovery
- Configuration files
- Database dumps
- Backup files
- Log files
- Source code

### 🎥 Exposed Devices
- IP cameras
- Webcams
- Printers
- Routers
- IoT devices

### 📄 Document Leaks
- Confidential PDFs
- Internal memos
- Financial reports
- Personal data
- Credentials

### 🗂️ Directory Exposure
- .git repositories
- .svn folders
- .env files
- Upload directories
- Backup folders

## Safety & Ethics

### ✅ DO
- Use for authorized security testing
- Respect robots.txt
- Follow terms of service
- Get permission before testing
- Report vulnerabilities responsibly

### ❌ DON'T
- Access unauthorized systems
- Download sensitive data without permission
- Exploit vulnerabilities
- Violate privacy
- Break laws

## Search Engine Differences

### Google
- Most comprehensive indexing
- Best for general searches
- Has rate limiting

### Bing
- Different index than Google
- Good alternative results
- Supports similar operators

### DuckDuckGo
- Privacy-focused
- Different results
- No tracking
- Limited advanced operators

## Rate Limiting Tips

1. **Pace Your Searches**
   - Don't search too rapidly
   - Wait between queries
   - Use different engines

2. **Use VPN if Blocked**
   - Rotate IP addresses
   - Use proxy services
   - Respect blocks

3. **Automate Responsibly**
   - Add delays between requests
   - Use User-Agent headers
   - Follow robots.txt

## Quick Command Reference

### Most Useful Combinations

1. `site:example.com filetype:pdf`
2. `site:example.com inurl:admin`
3. `site:*.example.com`
4. `intitle:"Index of" site:example.com`
5. `site:example.com (filetype:sql | filetype:env)`
6. `site:example.com intext:password`
7. `cache:example.com`
8. `related:example.com`
9. `link:example.com`
10. `site:example.com -inurl:www`

---

**Print this card for quick reference while dorking!**

🔍 Happy Searching! 🎯
