# Start Backend and Frontend Servers

Write-Host "🚀 Starting Advanced Dorking Tool..." -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = & python --version 2>&1
    Write-Host "✓ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Python not found. Please install Python 3.7+" -ForegroundColor Red
    exit 1
}

# Check if Node.js is installed
try {
    $nodeVersion = & node --version 2>&1
    Write-Host "✓ Node.js found: $nodeVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Node.js not found. Please install Node.js 14+" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "📦 Installing dependencies..." -ForegroundColor Yellow

# Install backend dependencies
Write-Host "Installing Python packages..." -ForegroundColor Cyan
Set-Location backend
pip install -r requirements.txt --quiet
Set-Location ..

# Install frontend dependencies if needed
if (-Not (Test-Path "frontend\node_modules")) {
    Write-Host "Installing Node packages..." -ForegroundColor Cyan
    Set-Location frontend
    npm install --silent
    Set-Location ..
}

Write-Host ""
Write-Host "🎯 Starting servers..." -ForegroundColor Yellow
Write-Host ""

# Start backend in a new PowerShell window
$backendScript = "cd '$PWD\backend'; python dorking_tool.py"
Start-Process powershell -ArgumentList "-NoExit", "-Command", $backendScript

Start-Sleep -Seconds 2

# Start frontend in a new PowerShell window
$frontendScript = "cd '$PWD\frontend'; npm run dev"
Start-Process powershell -ArgumentList "-NoExit", "-Command", $frontendScript

Write-Host ""
Write-Host "✅ Servers starting..." -ForegroundColor Green
Write-Host ""
Write-Host "Backend API: http://localhost:8000" -ForegroundColor Cyan
Write-Host "Frontend UI: http://localhost:5173" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press any key to exit..." -ForegroundColor Yellow
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
