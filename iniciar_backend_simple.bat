@echo off
echo ========================================
echo   Iniciando Backend NutriLife
echo ========================================
echo.

cd /d "%~dp0"

echo Activando entorno virtual...
call .venv\Scripts\activate.bat

echo.
echo Iniciando servidor Flask...
echo.
echo Servidor corriendo en: http://localhost:5000
echo Presiona Ctrl+C para detener el servidor
echo.

python backend\app.py

pause

