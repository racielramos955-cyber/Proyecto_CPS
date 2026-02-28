@echo off
echo ========================================
echo   Iniciando Frontend NutriLife
echo ========================================
echo.

cd /d "%~dp0"

REM Intentar usar Python del entorno virtual primero
if exist ".venv\Scripts\python.exe" (
    echo Usando Python del entorno virtual...
    cd frontend
    "%~dp0.venv\Scripts\python.exe" -m http.server 8000
) else (
    REM Si no existe, intentar Python del sistema
    cd frontend
    python -m http.server 8000
)

pause

