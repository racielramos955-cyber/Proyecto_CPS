# Script para iniciar el frontend accesible desde la red local
# Este script detecta tu IP local y muestra las URLs para acceder

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Iniciando Frontend NutriLife" -ForegroundColor Cyan
Write-Host "  (Accesible desde Red Local)" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Cambiar al directorio del proyecto
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

# Obtener IP local
$ipLocal = (Get-NetIPAddress -AddressFamily IPv4 | Where-Object {
    ($_.IPAddress -like "192.168.*" -or $_.IPAddress -like "10.*") -and 
    $_.IPAddress -notlike "192.168.106.*" -and 
    $_.IPAddress -notlike "192.168.35.*"
} | Select-Object -First 1).IPAddress

if (-not $ipLocal) {
    $ipLocal = "TU_IP_LOCAL"
    Write-Host "[ADVERTENCIA] No se pudo detectar IP local automáticamente" -ForegroundColor Yellow
    Write-Host "              Usa: ipconfig para encontrar tu IP" -ForegroundColor Yellow
    Write-Host ""
}

# Verificar que existe la carpeta frontend
if (-not (Test-Path "frontend")) {
    Write-Host "[ERROR] No se encontro la carpeta frontend" -ForegroundColor Red
    pause
    exit 1
}

# Cambiar a la carpeta frontend
Set-Location frontend

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "  URLs de Acceso:" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host "  Local:     http://localhost:8000" -ForegroundColor White
Write-Host "  Red Local: http://$ipLocal:8000" -ForegroundColor White
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "  Servidor escuchando en: 0.0.0.0:8000" -ForegroundColor Cyan
Write-Host "  (Acepta conexiones desde cualquier IP)" -ForegroundColor Gray
Write-Host ""
Write-Host "  Presiona Ctrl+C para detener el servidor" -ForegroundColor Yellow
Write-Host ""

# Verificar si Python está disponible
try {
    $pythonVersion = python --version 2>&1
} catch {
    # Intentar usar Python del entorno virtual
    if (Test-Path "..\venv\Scripts\python.exe") {
        $pythonPath = "..\venv\Scripts\python.exe"
    } elseif (Test-Path "..\.venv\Scripts\python.exe") {
        $pythonPath = "..\.venv\Scripts\python.exe"
    } else {
        Write-Host "[ERROR] Python no encontrado" -ForegroundColor Red
        Write-Host "[SOLUCION] Instala Python o agrega Python al PATH" -ForegroundColor Yellow
        pause
        exit 1
    }
}

# Ejecutar el servidor HTTP con bind a todas las interfaces
try {
    if ($pythonPath) {
        & $pythonPath -m http.server 8000 --bind 0.0.0.0
    } else {
        python -m http.server 8000 --bind 0.0.0.0
    }
} catch {
    Write-Host ""
    Write-Host "[ERROR] Error al ejecutar el servidor HTTP:" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
    Write-Host ""
    Write-Host "[SOLUCION] Verifica que:" -ForegroundColor Yellow
    Write-Host "  1. Python este instalado" -ForegroundColor Yellow
    Write-Host "  2. El puerto 8000 no este en uso" -ForegroundColor Yellow
    Write-Host "  3. Tienes permisos para usar el puerto 8000" -ForegroundColor Yellow
    Write-Host ""
    pause
}

