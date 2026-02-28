# Script para iniciar el backend accesible desde la red local
# Este script detecta tu IP local y muestra las URLs para acceder

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Iniciando Backend NutriLife" -ForegroundColor Cyan
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

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "  URLs de Acceso:" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host "  Local:     http://localhost:5000" -ForegroundColor White
Write-Host "  Red Local: http://$ipLocal:5000" -ForegroundColor White
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "[2/2] Iniciando servidor Flask..." -ForegroundColor Yellow
Write-Host ""
Write-Host "  Servidor escuchando en: 0.0.0.0:5000" -ForegroundColor Cyan
Write-Host "  (Acepta conexiones desde cualquier IP)" -ForegroundColor Gray
Write-Host ""
Write-Host "  Presiona Ctrl+C para detener el servidor" -ForegroundColor Yellow
Write-Host ""

# Ejecutar el backend
try {
    python backend\app.py
} catch {
    Write-Host ""
    Write-Host "[ERROR] Error al ejecutar el backend:" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
    Write-Host ""
    pause
}

