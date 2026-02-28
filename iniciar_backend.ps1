# Script para iniciar el backend de NutriLife
# Este script activa el entorno virtual y ejecuta el backend

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Iniciando Backend NutriLife" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Cambiar al directorio del proyecto
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

# Verificar que existe el entorno virtual
if (-not (Test-Path ".venv")) {
    Write-Host "[ERROR] No se encontro el entorno virtual .venv" -ForegroundColor Red
    Write-Host "[SOLUCION] Ejecuta primero: .\configurar_proyecto.ps1" -ForegroundColor Yellow
    pause
    exit 1
}

# Activar entorno virtual
Write-Host "[1/2] Activando entorno virtual..." -ForegroundColor Yellow
& .venv\Scripts\Activate.ps1

if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] No se pudo activar el entorno virtual" -ForegroundColor Red
    pause
    exit 1
}

# Verificar que existe backend/app.py
if (-not (Test-Path "backend\app.py")) {
    Write-Host "[ERROR] No se encontro backend\app.py" -ForegroundColor Red
    pause
    exit 1
}

# Verificar que existe backend/.env
if (-not (Test-Path "backend\.env")) {
    Write-Host "[ADVERTENCIA] No se encontro backend\.env" -ForegroundColor Yellow
    Write-Host "[SOLUCION] Copia credenciales\backend.env a backend\.env" -ForegroundColor Yellow
    Write-Host ""
}

Write-Host "[2/2] Iniciando servidor Flask..." -ForegroundColor Yellow
Write-Host ""
Write-Host "Servidor iniciando en: http://localhost:5000" -ForegroundColor Green
Write-Host "Presiona Ctrl+C para detener el servidor" -ForegroundColor Yellow
Write-Host ""

# Ejecutar el backend
try {
    python backend\app.py
} catch {
    Write-Host ""
    Write-Host "[ERROR] Error al ejecutar el backend:" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
    Write-Host ""
    Write-Host "[SOLUCION] Verifica que:" -ForegroundColor Yellow
    Write-Host "  1. El entorno virtual este activado" -ForegroundColor Yellow
    Write-Host "  2. Las dependencias esten instaladas (pip install -r requirements.txt)" -ForegroundColor Yellow
    Write-Host "  3. El puerto 5000 no este en uso" -ForegroundColor Yellow
    Write-Host ""
    pause
}

