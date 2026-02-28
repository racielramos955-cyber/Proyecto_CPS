@echo off
echo ========================================
echo   Iniciando Frontend NutriLife
echo ========================================
echo.

REM Cambiar al directorio del script
cd /d "%~dp0"

REM Verificar que existe la carpeta frontend
if not exist "frontend" (
    echo ERROR: No se encontro la carpeta frontend
    echo.
    echo Asegurate de estar en el directorio correcto:
    echo C:\Proyecto IA\IBM_Inteligente
    echo.
    pause
    exit /b 1
)

REM Cambiar a la carpeta frontend
cd frontend

echo Iniciando servidor HTTP en puerto 8000...
echo.
echo Servidor iniciando en: http://localhost:8000
echo.
echo Presiona Ctrl+C para detener el servidor
echo.

REM Intentar usar Python del entorno virtual primero
if exist "..\venv\Scripts\python.exe" (
    echo Usando Python del entorno virtual...
    "..\venv\Scripts\python.exe" -m http.server 8000
) else if exist "..\.venv\Scripts\python.exe" (
    echo Usando Python del entorno virtual...
    "..\.venv\Scripts\python.exe" -m http.server 8000
) else (
    REM Si no existe, intentar Python del sistema
    python -m http.server 8000
)

pause

