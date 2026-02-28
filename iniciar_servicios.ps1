# Script simple para iniciar backend y frontend
# Este script inicia ambos servicios en ventanas separadas

$projectPath = "C:\Proyecto IA\IBM_Inteligente"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Iniciando NutriLife AI + Web3" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar que estamos en el directorio correcto
if (-not (Test-Path "$projectPath\.venv")) {
    Write-Host "[ERROR] No se encontro el entorno virtual en: $projectPath" -ForegroundColor Red
    Write-Host "Verifica que estas en el directorio correcto del proyecto" -ForegroundColor Yellow
    pause
    exit 1
}

Write-Host "[1/2] Iniciando Backend..." -ForegroundColor Yellow

# Iniciar Backend
$backendScript = @"
cd '$projectPath'
& '$projectPath\.venv\Scripts\python.exe' backend\app.py
"@

Start-Process powershell -ArgumentList "-NoExit", "-Command", $backendScript -WindowStyle Normal

Write-Host "   Backend iniciando en: http://localhost:5000" -ForegroundColor Green
Write-Host ""

# Esperar un poco para que el backend inicie
Start-Sleep -Seconds 5

Write-Host "[2/2] Iniciando Frontend..." -ForegroundColor Yellow

# Iniciar Frontend
$frontendScript = @"
cd '$projectPath\frontend'
python -m http.server 8000
"@

Start-Process powershell -ArgumentList "-NoExit", "-Command", $frontendScript -WindowStyle Normal

Write-Host "   Frontend iniciando en: http://localhost:8000" -ForegroundColor Green
Write-Host ""

# Esperar un poco más
Start-Sleep -Seconds 3

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Servicios iniciados" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Backend:  http://localhost:5000" -ForegroundColor White
Write-Host "Frontend: http://localhost:8000" -ForegroundColor White
Write-Host ""
Write-Host "Abriendo navegador..." -ForegroundColor Yellow

# Abrir navegador
Start-Process "http://localhost:8000"

Write-Host ""
Write-Host "Presiona cualquier tecla para cerrar esta ventana..." -ForegroundColor Gray
Write-Host "(Los servicios seguiran corriendo en otras ventanas)" -ForegroundColor Gray
Write-Host ""
pause

