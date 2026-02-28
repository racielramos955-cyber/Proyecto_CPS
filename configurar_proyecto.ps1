# Script de configuracion automatica para NutriLife AI + Web3
# Ejecuta este script para configurar el proyecto automaticamente

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Configuracion de NutriLife AI + Web3" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar Python
Write-Host "[1/5] Verificando Python..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "OK Python encontrado: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "ERROR Python no encontrado. Por favor instala Python 3.8 o superior." -ForegroundColor Red
    exit 1
}

# Crear entorno virtual si no existe
Write-Host ""
Write-Host "[2/5] Configurando entorno virtual..." -ForegroundColor Yellow
if (Test-Path ".venv") {
    Write-Host "OK Entorno virtual ya existe" -ForegroundColor Green
} else {
    Write-Host "Creando entorno virtual..." -ForegroundColor Yellow
    python -m venv .venv
    if ($LASTEXITCODE -eq 0) {
        Write-Host "OK Entorno virtual creado" -ForegroundColor Green
    } else {
        Write-Host "ERROR Error al crear entorno virtual" -ForegroundColor Red
        exit 1
    }
}

# Activar entorno virtual e instalar dependencias
Write-Host ""
Write-Host "[3/5] Instalando dependencias..." -ForegroundColor Yellow
& .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
Write-Host "Instalando paquetes (esto puede tardar varios minutos)..." -ForegroundColor Yellow
pip install -r requirements.txt
if ($LASTEXITCODE -eq 0) {
    Write-Host "OK Dependencias instaladas" -ForegroundColor Green
} else {
    Write-Host "ADVERTENCIA Hubo algunos errores al instalar dependencias" -ForegroundColor Yellow
}

# Configurar credenciales
Write-Host ""
Write-Host "[4/5] Configurando credenciales..." -ForegroundColor Yellow

# Backend .env
if (Test-Path "backend\.env") {
    Write-Host "OK backend\.env ya existe" -ForegroundColor Green
} else {
    if (Test-Path "credenciales\backend.env") {
        Copy-Item "credenciales\backend.env" "backend\.env"
        Write-Host "OK backend\.env creado desde credenciales" -ForegroundColor Green
    } else {
        Write-Host "ADVERTENCIA No se encontro credenciales\backend.env" -ForegroundColor Yellow
        Write-Host "   Necesitaras crear backend\.env manualmente" -ForegroundColor Yellow
    }
}

# Frontend contract-config.js
if (Test-Path "frontend\js\contract-config.js") {
    Write-Host "OK frontend\js\contract-config.js ya existe" -ForegroundColor Green
} else {
    if (Test-Path "credenciales\contract-config.js") {
        Copy-Item "credenciales\contract-config.js" "frontend\js\contract-config.js"
        Write-Host "OK frontend\js\contract-config.js creado desde credenciales" -ForegroundColor Green
    } else {
        Write-Host "ADVERTENCIA No se encontro credenciales\contract-config.js" -ForegroundColor Yellow
    }
}

# Frontend NutriLifeABI.json
if (Test-Path "frontend\js\NutriLifeABI.json") {
    Write-Host "OK frontend\js\NutriLifeABI.json ya existe" -ForegroundColor Green
} else {
    if (Test-Path "credenciales\NutriLifeABI.json") {
        Copy-Item "credenciales\NutriLifeABI.json" "frontend\js\NutriLifeABI.json"
        Write-Host "OK frontend\js\NutriLifeABI.json creado desde credenciales" -ForegroundColor Green
    } else {
        Write-Host "ADVERTENCIA No se encontro credenciales\NutriLifeABI.json" -ForegroundColor Yellow
    }
}

# Verificar instalacion
Write-Host ""
Write-Host "[5/5] Verificando instalacion..." -ForegroundColor Yellow
python verificar_instalacion.py

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  OK Configuracion completada!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Para iniciar la aplicacion:" -ForegroundColor Yellow
Write-Host "   1. Ejecuta: .\iniciar_todo.bat" -ForegroundColor White
Write-Host "   2. O manualmente:" -ForegroundColor White
Write-Host "      Terminal 1: .venv\Scripts\Activate.ps1; python backend\app.py" -ForegroundColor White
Write-Host "      Terminal 2: cd frontend; python -m http.server 8000" -ForegroundColor White
Write-Host ""
Write-Host "Lee GUIA_INSTALACION.md para mas detalles" -ForegroundColor Yellow
Write-Host ""
