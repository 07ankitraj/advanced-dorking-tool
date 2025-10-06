# 🔍 Advanced Google Dorking Tool

The most powerful and comprehensive Google Dorking tool ever created! This tool combines the power of advanced search operators with a beautiful, intuitive interface.

## ✨ Features

### 🎯 Core Functionality
- **Multi-Engine Search**: Search across Google, Bing, and DuckDuckGo
- **Predefined Templates**: 8 categories with 40+ ready-to-use dork queries
- **Custom Dork Builder**: Build complex queries with an intuitive form interface
- **Real-time Results**: Get instant search results with clean formatting
- **Export Functionality**: Export search results to JSON for further analysis

### 📋 Template Categories
1. **SQL Injection** - Find potential SQL injection vulnerabilities
2. **Exposed Files** - Discover sensitive files and configurations
3. **Admin Panels** - Locate admin login pages and dashboards
4. **Exposed Cameras** - Find publicly accessible webcams
5. **Sensitive Directories** - Discover exposed directories and configs
6. **Exposed Documents** - Find confidential PDFs and documents
7. **Login Pages** - Locate authentication pages
8. **Error Messages** - Find pages with exposed error information

### 🛠️ Dork Operators Supported
- `site:` - Search within specific domains
- `filetype:` - Find specific file types
- `inurl:` - Search for terms in URLs
- `intitle:` - Search for terms in page titles
- `intext:` - Search for terms in page content
- `ext:` - Search by file extension
- `link:` - Find pages linking to a URL
- `related:` - Find related websites
- `cache:` - View cached versions
- `allintitle:`, `allinurl:`, `allintext:` - All terms operators

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7+
- Node.js 14+
- npm or yarn

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create and activate a virtual environment:
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. Install Python dependencies:
```bash
pip install fastapi uvicorn requests beautifulsoup4 pydantic
```

4. Run the FastAPI server:
```bash
python dorking_tool.py
```

The backend API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The frontend will be available at `http://localhost:5173`

## 📖 Usage Guide

### Search Tab
1. Enter your dork query in the text area
2. Select your preferred search engine (Google/Bing/DuckDuckGo)
3. Choose the number of results (1-50)
4. Click "Search" to execute the query
5. View results with titles, URLs, and snippets
6. Export results to JSON if needed

### Templates Tab
1. Browse through 8 categories of predefined dorks
2. Click any dork query to automatically use it in search
3. Perfect for beginners or quick searches

### Dork Builder Tab
1. Fill in the form fields with your search criteria
2. Use any combination of operators
3. Click "Build Dork Query" to generate the query
4. Use the generated query immediately or copy it

### Operators Guide Tab
1. Learn about all available dork operators
2. See examples for each operator
3. Understand how to combine operators effectively

## 🎨 API Endpoints

### GET `/`
- Health check and API information

### GET `/templates`
- Returns all predefined dork templates

### GET `/templates/{category}`
- Returns templates for a specific category

### POST `/search`
- Execute a dork query
- Body: `{"query": "...", "engine": "google", "num_results": 10}`

### POST `/build-dork`
- Build a custom dork query from parameters
- Body: `{"site": "...", "filetype": "...", ...}`

### GET `/operators`
- Returns list of all available dork operators with descriptions

## ⚠️ Ethical Usage Guidelines

This tool is designed for:
- Security research and penetration testing (with permission)
- Information gathering for legitimate purposes
- Educational and learning purposes
- OSINT (Open Source Intelligence) investigations

**DO NOT use this tool for:**
- Illegal activities
- Unauthorized access to systems
- Privacy violations
- Malicious purposes

Always:
- Obtain proper authorization before testing systems
- Respect privacy and data protection laws
- Follow responsible disclosure practices
- Use for ethical and legal purposes only

## 🔒 Privacy & Security

- All searches are performed client-side through public search engines
- No user data is stored or logged
- Results are not cached or saved by the application
- Use responsibly and respect robots.txt and terms of service

## 🛡️ Legal Disclaimer

This tool is provided for educational and research purposes only. The developers are not responsible for any misuse or illegal activities performed with this tool. Users are solely responsible for their actions and must comply with all applicable laws and regulations.

## 🌟 Advanced Tips

### Combining Operators
```
site:example.com filetype:pdf "confidential"
```

### Excluding Terms
```
site:example.com -inurl:login
```

### OR Operator
```
site:example.com (admin | login)
```

### Wildcards
```
site:*.example.com
```

### Number Ranges
```
filetype:pdf "report" 2020..2024
```

## 🔧 Troubleshooting

### Backend won't start
- Ensure Python 3.7+ is installed
- Check if port 8000 is available
- Verify all dependencies are installed

### Frontend won't connect
- Ensure backend is running on port 8000
- Check CORS settings if issues persist
- Verify API_URL in App.jsx matches backend

### No search results
- Some search engines may block automated requests
- Try different search engines
- Use more specific queries
- Be patient with rate limits

## 🚀 Future Enhancements

- [ ] Proxy support for anonymity
- [ ] Rate limiting and request throttling
- [ ] Advanced result filtering
- [ ] Screenshot capture of results
- [ ] Export to CSV/Excel
- [ ] Search history and saved queries
- [ ] Batch query execution
- [ ] API key support for official APIs
- [ ] Dark mode theme
- [ ] Multi-language support

## 📝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📜 License

This project is for educational purposes. Use at your own risk and responsibility.

## 🤝 Acknowledgments

- FastAPI for the amazing backend framework
- React + Vite for the modern frontend stack
- BeautifulSoup for web scraping capabilities
- The security research community for dorking techniques

---

**Remember: With great power comes great responsibility. Use this tool ethically and legally.**

🔍 Happy Dorking! 🔍
