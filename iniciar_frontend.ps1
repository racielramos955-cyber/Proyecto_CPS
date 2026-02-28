# Script para iniciar el frontend de NutriLife
# Este script inicia el servidor HTTP para el frontend

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Iniciando Frontend NutriLife" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Cambiar al directorio del proyecto
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

# Verificar que existe la carpeta frontend
if (-not (Test-Path "frontend")) {
    Write-Host "[ERROR] No se encontro la carpeta frontend" -ForegroundColor Red
    pause
    exit 1
}

# Cambiar a la carpeta frontend
Set-Location frontend

# Verificar que existe index.html
if (-not (Test-Path "index.html")) {
    Write-Host "[ERROR] No se encontro index.html en frontend" -ForegroundColor Red
    pause
    exit 1
}

Write-Host "Iniciando servidor HTTP en puerto 8000..." -ForegroundColor Yellow
Write-Host ""
Write-Host "Servidor iniciando en: http://localhost:8000" -ForegroundColor Green
Write-Host "Presiona Ctrl+C para detener el servidor" -ForegroundColor Yellow
Write-Host ""

# Verificar si Python está disponible
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Usando: $pythonVersion" -ForegroundColor Gray
    Write-Host ""
} catch {
    Write-Host "[ERROR] Python no encontrado" -ForegroundColor Red
    Write-Host "[SOLUCION] Instala Python o agrega Python al PATH" -ForegroundColor Yellow
    pause
    exit 1
}

# Ejecutar el servidor HTTP
try {
    python -m http.server 8000
} catch {
    Write-Host ""
    Write-Host "[ERROR] Error al ejecutar el servidor HTTP:" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
    Write-Host ""
    Write-Host "[SOLUCION] Verifica que:" -ForegroundColor Yellow
    Write-Host "  1. Python este instalado y en el PATH" -ForegroundColor Yellow
    Write-Host "  2. El puerto 8000 no este en uso" -ForegroundColor Yellow
    Write-Host "  3. Tienes permisos para usar el puerto 8000" -ForegroundColor Yellow
    Write-Host ""
    pause
}

