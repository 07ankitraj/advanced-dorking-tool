# 🎯 Example Dork Queries - Real-World Scenarios

## 🔐 Security Research (With Permission)

### Finding Exposed Configuration Files
```
site:target.com (filetype:env | filetype:config | filetype:ini)
site:target.com intext:"DB_PASSWORD" | intext:"API_KEY"
site:target.com ext:env "database" | "password"
```

### Finding Exposed Database Files
```
site:target.com filetype:sql intext:password
site:target.com ext:sql "INSERT INTO"
site:target.com filetype:db
```

### Finding Backup Files
```
site:target.com (filetype:bak | filetype:backup | filetype:old)
site:target.com inurl:backup
site:target.com (inurl:old | inurl:backup | inurl:bak)
```

### Finding Log Files
```
site:target.com filetype:log
site:target.com ext:log intext:error
site:target.com inurl:logs
```

### Finding Error Pages
```
site:target.com (intitle:"error" | intitle:"warning")
site:target.com intext:"SQL syntax error"
site:target.com intext:"Warning: mysql_connect"
site:target.com intext:"Fatal error"
```

### Finding Admin Panels
```
site:target.com inurl:admin
site:target.com inurl:administrator
site:target.com intitle:"admin login"
site:target.com (inurl:admin | inurl:login | inurl:dashboard)
```

### Finding Login Pages
```
site:target.com intitle:login
site:target.com inurl:login.php
site:target.com (inurl:signin | inurl:login | inurl:auth)
```

### Finding Upload Directories
```
site:target.com intitle:"Index of" upload
site:target.com inurl:upload
site:target.com (inurl:upload | inurl:uploads | inurl:files)
```

### Finding Test/Dev Environments
```
site:target.com (inurl:test | inurl:dev | inurl:staging)
site:target.com (subdomain:test | subdomain:dev | subdomain:staging)
site:*.target.com (test | dev | staging)
```

### Finding Exposed Git Repositories
```
site:target.com inurl:.git
intitle:"Index of" .git site:target.com
site:target.com intitle:"Index of" .git/config
```

## 🕵️ OSINT (Open Source Intelligence)

### Finding Social Media Profiles
```
"target.com" site:twitter.com
"target.com" site:linkedin.com
"target.com" site:facebook.com
"target company" (site:twitter.com | site:linkedin.com | site:facebook.com)
```

### Finding Email Addresses
```
site:target.com intext:"@target.com"
site:target.com "@target.com" (email | contact | mailto)
"@target.com" -site:target.com
```

### Finding Phone Numbers
```
site:target.com intext:"phone" | intext:"tel" | intext:"call"
site:target.com (phone | telephone | mobile) (number | contact)
```

### Finding Employee Information
```
site:linkedin.com "target company" (employee | works at | working at)
site:target.com inurl:team | inurl:about | inurl:staff
```

### Finding Company Documents
```
site:target.com (filetype:pdf | filetype:doc | filetype:ppt)
site:target.com filetype:pdf (report | presentation | whitepaper)
"target company" filetype:pdf
```

### Finding Press Releases
```
site:target.com inurl:press | inurl:news | inurl:media
"target company" (press release | announcement | news)
```

### Finding Job Postings
```
site:target.com inurl:careers | inurl:jobs | inurl:hiring
"target company" (hiring | job opening | career opportunity)
```

### Finding Presentations
```
site:target.com filetype:ppt | filetype:pptx
"target company" filetype:ppt
site:slideshare.net "target company"
```

## 📄 Content Discovery

### Finding Research Papers
```
filetype:pdf (machine learning | artificial intelligence)
filetype:pdf "research paper" (neural networks | deep learning)
filetype:pdf author:"researcher name"
```

### Finding Datasets
```
filetype:csv dataset
filetype:json data | dataset
intitle:"Index of" (csv | json | dataset)
```

### Finding eBooks
```
filetype:pdf (ebook | book) -buy -amazon
filetype:epub (title | author)
intitle:"Index of" (pdf | epub) books
```

### Finding Code Examples
```
site:github.com "code example"
site:stackoverflow.com "how to"
filetype:py | filetype:js "example"
```

### Finding Academic Resources
```
site:edu filetype:pdf
site:.edu (research | study | thesis)
filetype:pdf site:edu (subject area)
```

### Finding Government Data
```
site:gov filetype:pdf | filetype:xls
site:.gov (data | statistics | report)
intitle:"Index of" site:gov
```

### Finding Medical Information
```
site:nih.gov | site:who.int
filetype:pdf (medical | health | disease)
site:.edu (medicine | medical research)
```

### Finding Legal Documents
```
filetype:pdf (contract | agreement | terms)
site:gov filetype:pdf (law | regulation)
filetype:pdf (legal | court | case)
```

## 💼 Competitive Intelligence

### Finding Technology Stack
```
site:competitor.com intext:"powered by"
site:competitor.com intext:"built with"
site:competitor.com (wordpress | drupal | joomla | react | angular)
```

### Finding Job Postings (Tech Stack)
```
site:competitor.com inurl:careers (python | java | react | node)
"competitor company" job posting (required skills | technologies)
```

### Finding Partners/Clients
```
site:competitor.com (partner | client | customer)
"competitor company" (partnership | collaboration)
```

### Finding Product Information
```
site:competitor.com (product | service | solution)
site:competitor.com inurl:product | inurl:pricing
```

### Finding Marketing Materials
```
site:competitor.com (brochure | datasheet | whitepaper)
"competitor company" filetype:pdf (marketing | case study)
```

### Finding Financial Information
```
"competitor company" (revenue | earnings | financial)
site:competitor.com inurl:investor | inurl:financial
```

### Finding News Mentions
```
"competitor company" site:news.google.com
"competitor company" (acquisition | merger | partnership)
```

### Finding Patents
```
site:patents.google.com "competitor company"
"competitor company" (patent | invention)
```

## 🌐 Subdomain Discovery

### Finding All Subdomains
```
site:*.target.com
site:*.target.com -site:www.target.com
site:*.*.target.com
```

### Finding Development Subdomains
```
site:*.target.com (dev | test | staging | beta)
site:dev.target.com | site:test.target.com | site:staging.target.com
```

### Finding Internal Subdomains
```
site:*.target.com (internal | intranet | vpn)
site:*.target.com (admin | portal | dashboard)
```

### Finding API Endpoints
```
site:*.target.com (api | rest | graphql)
site:api.target.com
```

## 🎓 Educational Research

### Finding Course Materials
```
site:.edu filetype:pdf (syllabus | lecture | course)
site:.edu (tutorial | guide | howto)
```

### Finding Thesis/Dissertations
```
site:.edu filetype:pdf (thesis | dissertation)
filetype:pdf (master thesis | phd thesis)
```

### Finding Lecture Notes
```
site:.edu (notes | lectures | slides)
site:.edu filetype:pdf | filetype:ppt
```

### Finding Study Guides
```
filetype:pdf "study guide"
site:.edu (exam | test | quiz) guide
```

## 🔧 Technical Discovery

### Finding API Documentation
```
site:target.com (api | documentation | docs)
site:target.com inurl:api | inurl:docs
```

### Finding Source Code
```
site:github.com "target.com"
site:gitlab.com "target.com"
site:bitbucket.org "target.com"
```

### Finding Developer Resources
```
site:target.com (developer | dev | sdk)
site:target.com inurl:developer | inurl:api
```

### Finding Swagger/OpenAPI Docs
```
site:target.com (swagger | openapi)
site:target.com inurl:swagger-ui
```

## 🎥 Media Discovery

### Finding Videos
```
site:youtube.com "topic"
site:vimeo.com "topic"
intitle:"topic" site:dailymotion.com
```

### Finding Images
```
filetype:jpg | filetype:png "topic"
intitle:"Index of" (jpg | png | gif)
```

### Finding Audio Files
```
filetype:mp3 | filetype:wav "topic"
intitle:"Index of" (mp3 | music)
```

### Finding Podcasts
```
site:podcasts.apple.com "topic"
site:spotify.com podcast "topic"
```

## 🏢 Corporate Research

### Finding Company Information
```
"company name" (about | overview | profile)
site:crunchbase.com "company name"
site:linkedin.com/company/ "company name"
```

### Finding Annual Reports
```
"company name" filetype:pdf (annual report | 10-K)
site:company.com filetype:pdf annual report
```

### Finding Investor Relations
```
site:company.com inurl:investor
"company name" (investor relations | shareholders)
```

### Finding Acquisitions
```
"company name" (acquired | acquisition | bought)
"company name" site:news.google.com acquisition
```

## 🌍 Geographic Targeting

### Finding Location-Specific Content
```
site:target.com (location | address | city)
site:target.com intext:"city name"
```

### Finding Regional Sites
```
site:target.co.uk
site:target.de
site:target.fr
```

### Finding Maps/Locations
```
site:maps.google.com "company name"
site:target.com inurl:locations | inurl:store-finder
```

## 💡 Advanced Combinations

### Multi-Factor Search
```
site:target.com (filetype:pdf | filetype:doc) (confidential | internal) -public
```

### Time-Based Search
```
site:target.com 2024
site:target.com after:2024-01-01
```

### Complex Boolean Logic
```
site:target.com ((admin | administrator) AND (login | signin)) -test -demo
```

### Wildcard Combinations
```
site:*.target.com (admin | login) -www
```

### Exclusion Patterns
```
site:target.com -inurl:blog -inurl:news -inurl:support
```

## 🎯 Specialized Searches

### Finding Cameras/IoT Devices
```
inurl:"view/index.shtml"
intitle:"Network Camera"
inurl:"MultiCameraFrame?Mode="
intitle:"webcamXP 5"
```

### Finding Printers
```
intitle:"HP LaserJet" inurl:hp/device
intitle:"printer" inurl:status
```

### Finding Routers
```
intitle:"Router" login
intitle:"DD-WRT"
inurl:cgi-bin/luci
```

### Finding FTP Servers
```
intitle:"Index of" inurl:ftp
intitle:"FTP" inurl:login
```

### Finding Database Admin Panels
```
intitle:"phpMyAdmin"
intitle:"Adminer"
inurl:phpmyadmin
```

## 🔍 Miscellaneous

### Finding RSS Feeds
```
site:target.com filetype:xml rss
site:target.com inurl:feed | inurl:rss
```

### Finding Sitemaps
```
site:target.com filetype:xml sitemap
site:target.com inurl:sitemap.xml
```

### Finding Robots.txt
```
site:target.com inurl:robots.txt
```

### Finding .htaccess Files
```
intitle:"Index of" .htaccess
```

### Finding WordPress Sites
```
inurl:wp-content
intitle:"WordPress"
site:target.com /wp-admin/
```

## ⚠️ Important Reminders

### Always Remember:
1. **Get Permission**: Only test systems you own or have permission to test
2. **Respect Privacy**: Don't access or download unauthorized data
3. **Follow Laws**: Obey all applicable laws and regulations
4. **Be Ethical**: Use for legitimate purposes only
5. **Report Responsibly**: If you find vulnerabilities, report them properly

### Best Practices:
- Start with broad searches, then narrow down
- Verify results manually
- Document your findings
- Use multiple search engines
- Respect rate limits
- Don't automate excessively

## 💡 Tips for Better Results

1. **Combine Operators**: Use multiple operators together
2. **Use Parentheses**: Group related terms
3. **Try Variations**: Different phrasings yield different results
4. **Check Multiple Engines**: Each engine has different indexes
5. **Be Specific**: More specific queries = better results
6. **Use Quotes**: Exact phrase matching is powerful
7. **Exclude Noise**: Use minus to remove irrelevant results
8. **Think Creatively**: Consider what you're really looking for

---

## 🎯 Quick Copy-Paste Templates

Replace `target.com` with your target domain:

```
# Security Audit Template
site:target.com (filetype:env | filetype:config | filetype:sql | filetype:bak)

# Subdomain Discovery Template
site:*.target.com -site:www.target.com

# Document Discovery Template
site:target.com (filetype:pdf | filetype:doc | filetype:xls)

# Admin Panel Discovery Template
site:target.com (inurl:admin | inurl:login | intitle:"admin")

# Error Page Discovery Template
site:target.com (intitle:"error" | intext:"SQL syntax" | intext:"Warning:")

# Backup Discovery Template
site:target.com (filetype:bak | filetype:backup | inurl:backup)

# Upload Directory Discovery Template
site:target.com (inurl:upload | intitle:"Index of" upload)

# Development Environment Discovery Template
site:target.com (inurl:test | inurl:dev | inurl:staging)
```

---

**Use these examples responsibly and ethically!**

🔍 Happy Dorking! 🎯
