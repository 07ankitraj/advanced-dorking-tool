import { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [activeTab, setActiveTab] = useState('search');
  const [searchQuery, setSearchQuery] = useState('');
  const [searchEngine, setSearchEngine] = useState('google');
  const [numResults, setNumResults] = useState(10);
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [templates, setTemplates] = useState({});
  const [selectedCategory, setSelectedCategory] = useState('');
  const [operators, setOperators] = useState([]);

  // Custom dork builder state
  const [customDork, setCustomDork] = useState({
    site: '',
    filetype: '',
    inurl: '',
    intitle: '',
    intext: '',
    ext: '',
    link: '',
    related: '',
    cache: '',
    allintitle: '',
    allinurl: '',
    allintext: ''
  });
  const [builtQuery, setBuiltQuery] = useState('');

  const API_URL = 'http://localhost:8000';

  useEffect(() => {
    fetchTemplates();
    fetchOperators();
  }, []);

  const fetchTemplates = async () => {
    try {
      const response = await fetch(`${API_URL}/templates`);
      const data = await response.json();
      setTemplates(data.templates);
    } catch (error) {
      console.error('Error fetching templates:', error);
    }
  };

  const fetchOperators = async () => {
    try {
      const response = await fetch(`${API_URL}/operators`);
      const data = await response.json();
      setOperators(data.operators);
    } catch (error) {
      console.error('Error fetching operators:', error);
    }
  };

  const handleSearch = async (query = searchQuery) => {
    if (!query.trim()) {
      alert('Please enter a search query');
      return;
    }

    setLoading(true);
    setResults([]);

    try {
      const response = await fetch(`${API_URL}/search`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          query: query,
          engine: searchEngine,
          num_results: numResults
        })
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      console.log('Search results:', data); // Debug log

      if (data.results && data.results.length > 0) {
        setResults(data.results);
      } else {
        setResults([]);
        alert('No results found. Try a different query or search engine.');
      }
    } catch (error) {
      console.error('Error searching:', error);
      alert('Search failed. Error: ' + error.message + '\n\nMake sure the backend server is running on http://localhost:8000');
      setResults([]);
    } finally {
      setLoading(false);
    }
  };

  const handleTemplateClick = (dork) => {
    setSearchQuery(dork);
    setActiveTab('search');
  };

  const handleBuildDork = async () => {
    try {
      const response = await fetch(`${API_URL}/build-dork`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(customDork)
      });

      const data = await response.json();
      setBuiltQuery(data.query);
      setSearchQuery(data.query);
    } catch (error) {
      console.error('Error building dork:', error);
    }
  };

  const handleCustomDorkChange = (field, value) => {
    setCustomDork(prev => ({
      ...prev,
      [field]: value
    }));
  };

  const exportResults = () => {
    const dataStr = JSON.stringify(results, null, 2);
    const dataBlob = new Blob([dataStr], { type: 'application/json' });
    const url = URL.createObjectURL(dataBlob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'dork-results.json';
    link.click();
  };

  return (
    <div className="App">
      <header className="header">
        <h1>🔍 Advanced Dorking Tool</h1>
        <p>The Ultimate Google Dorking & Search Intelligence Platform</p>
      </header>

      <div className="container">
        <div className="tabs">
          <button
            className={activeTab === 'search' ? 'tab active' : 'tab'}
            onClick={() => setActiveTab('search')}
          >
            🔎 Search
          </button>
          <button
            className={activeTab === 'templates' ? 'tab active' : 'tab'}
            onClick={() => setActiveTab('templates')}
          >
            📋 Templates
          </button>
          <button
            className={activeTab === 'builder' ? 'tab active' : 'tab'}
            onClick={() => setActiveTab('builder')}
          >
            🛠️ Dork Builder
          </button>
          <button
            className={activeTab === 'operators' ? 'tab active' : 'tab'}
            onClick={() => setActiveTab('operators')}
          >
            📚 Operators Guide
          </button>
        </div>

        {activeTab === 'search' && (
          <div className="tab-content">
            <div className="search-container">
              <h2>Search with Dork Query</h2>
              <textarea
                className="search-input"
                placeholder="Enter your dork query... (e.g., site:example.com filetype:pdf)"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                rows="3"
              />

              <div className="search-options">
                <div className="option-group">
                  <label>Search Engine:</label>
                  <select
                    value={searchEngine}
                    onChange={(e) => setSearchEngine(e.target.value)}
                    className="select-input"
                  >
                    <option value="google">Google</option>
                    <option value="bing">Bing</option>
                    <option value="duckduckgo">DuckDuckGo</option>
                  </select>
                </div>

                <div className="option-group">
                  <label>Results:</label>
                  <input
                    type="number"
                    min="1"
                    max="50"
                    value={numResults}
                    onChange={(e) => setNumResults(parseInt(e.target.value))}
                    className="number-input"
                  />
                </div>
              </div>

              <button
                className="btn btn-primary"
                onClick={() => handleSearch()}
                disabled={loading}
              >
                {loading ? '🔍 Searching...' : '🔍 Search'}
              </button>
            </div>

            {loading && (
              <div className="loading-message">
                <div className="spinner"></div>
                <p>Searching for results... Please wait</p>
              </div>
            )}

            {results.length > 0 && (
              <div className="results-container">
                <div className="results-header">
                  <h3>✅ Search Results ({results.length})</h3>
                  <button className="btn btn-secondary" onClick={exportResults}>
                    💾 Export Results
                  </button>
                </div>

                <div className="results-list">
                  {results.map((result, index) => (
                    <div key={index} className="result-item">
                      <div className="result-number">{index + 1}</div>
                      <h4>
                        <a href={result.url} target="_blank" rel="noopener noreferrer">
                          {result.title}
                        </a>
                      </h4>
                      <p className="result-url">🔗 {result.url}</p>
                      <p className="result-snippet">{result.snippet}</p>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        )}

        {activeTab === 'templates' && (
          <div className="tab-content">
            <h2>Predefined Dork Templates</h2>
            <p className="subtitle">Click any dork to use it in search</p>

            {Object.keys(templates).map(category => (
              <div key={category} className="template-category">
                <h3 className="category-title">
                  {category.split('_').map(word =>
                    word.charAt(0).toUpperCase() + word.slice(1)
                  ).join(' ')}
                </h3>
                <div className="dork-list">
                  {templates[category].map((dork, index) => (
                    <div
                      key={index}
                      className="dork-item"
                      onClick={() => handleTemplateClick(dork)}
                    >
                      <code>{dork}</code>
                    </div>
                  ))}
                </div>
              </div>
            ))}
          </div>
        )}

        {activeTab === 'builder' && (
          <div className="tab-content">
            <h2>Custom Dork Builder</h2>
            <p className="subtitle">Build your own custom dork query using operators</p>

            <div className="builder-form">
              <div className="form-grid">
                <div className="form-group">
                  <label>Site:</label>
                  <input
                    type="text"
                    placeholder="example.com"
                    value={customDork.site}
                    onChange={(e) => handleCustomDorkChange('site', e.target.value)}
                  />
                </div>

                <div className="form-group">
                  <label>File Type:</label>
                  <input
                    type="text"
                    placeholder="pdf, doc, xls"
                    value={customDork.filetype}
                    onChange={(e) => handleCustomDorkChange('filetype', e.target.value)}
                  />
                </div>

                <div className="form-group">
                  <label>In URL:</label>
                  <input
                    type="text"
                    placeholder="admin, login"
                    value={customDork.inurl}
                    onChange={(e) => handleCustomDorkChange('inurl', e.target.value)}
                  />
                </div>

                <div className="form-group">
                  <label>In Title:</label>
                  <input
                    type="text"
                    placeholder="login, admin"
                    value={customDork.intitle}
                    onChange={(e) => handleCustomDorkChange('intitle', e.target.value)}
                  />
                </div>

                <div className="form-group">
                  <label>In Text:</label>
                  <input
                    type="text"
                    placeholder="password, username"
                    value={customDork.intext}
                    onChange={(e) => handleCustomDorkChange('intext', e.target.value)}
                  />
                </div>

                <div className="form-group">
                  <label>Extension:</label>
                  <input
                    type="text"
                    placeholder="php, asp"
                    value={customDork.ext}
                    onChange={(e) => handleCustomDorkChange('ext', e.target.value)}
                  />
                </div>

                <div className="form-group">
                  <label>Link:</label>
                  <input
                    type="text"
                    placeholder="example.com"
                    value={customDork.link}
                    onChange={(e) => handleCustomDorkChange('link', e.target.value)}
                  />
                </div>

                <div className="form-group">
                  <label>Related:</label>
                  <input
                    type="text"
                    placeholder="example.com"
                    value={customDork.related}
                    onChange={(e) => handleCustomDorkChange('related', e.target.value)}
                  />
                </div>

                <div className="form-group">
                  <label>Cache:</label>
                  <input
                    type="text"
                    placeholder="example.com"
                    value={customDork.cache}
                    onChange={(e) => handleCustomDorkChange('cache', e.target.value)}
                  />
                </div>
              </div>

              <button className="btn btn-primary" onClick={handleBuildDork}>
                Build Dork Query
              </button>

              {builtQuery && (
                <div className="built-query">
                  <h3>Generated Query:</h3>
                  <div className="query-box">
                    <code>{builtQuery}</code>
                  </div>
                  <button
                    className="btn btn-secondary"
                    onClick={() => {
                      handleSearch(builtQuery);
                      setActiveTab('search');
                    }}
                  >
                    Search with This Query
                  </button>
                </div>
              )}
            </div>
          </div>
        )}

        {activeTab === 'operators' && (
          <div className="tab-content">
            <h2>Google Dork Operators Guide</h2>
            <p className="subtitle">Learn how to use advanced search operators</p>

            <div className="operators-list">
              {operators.map((operator, index) => (
                <div key={index} className="operator-item">
                  <h3>{operator.name}</h3>
                  <p>{operator.description}</p>
                  <div className="example">
                    <strong>Example:</strong> <code>{operator.example}</code>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>

      <footer className="footer">
        <p>⚠️ Use responsibly and ethically. Respect privacy and follow applicable laws.</p>
      </footer>
    </div>
  );
}

export default App;
