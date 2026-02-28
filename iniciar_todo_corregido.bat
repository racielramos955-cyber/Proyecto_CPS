@echo off
echo ========================================
echo   NutriLife AI + Web3
echo   Iniciando Backend y Frontend
echo ========================================
echo.

REM Cambiar al directorio del script
cd /d "%~dp0"

REM Verificar que existe .venv
if not exist .venv (
    echo.
    echo ERROR: No se encontro el entorno virtual .venv
    echo.
    echo Por favor, ejecuta primero: configurar_proyecto.ps1
    echo.
    pause
    exit /b 1
)

echo [1/2] Iniciando Backend en http://localhost:5000
echo.
start "NutriLife Backend" powershell -ExecutionPolicy Bypass -File "%~dp0iniciar_backend.ps1"

REM Esperar un poco para que el backend inicie
timeout /t 5 /nobreak >nul

echo [2/2] Iniciando Frontend en http://localhost:8000
echo.
start "NutriLife Frontend" powershell -ExecutionPolicy Bypass -File "%~dp0iniciar_frontend.ps1"

echo.
echo ========================================
echo   Servicios iniciados
echo ========================================
echo.
echo   Backend:  http://localhost:5000
echo   Frontend: http://localhost:8000
echo.
echo   Presiona cualquier tecla para cerrar esta ventana...
echo   (Los servicios seguiran corriendo en otras ventanas)
echo.
pause >nul

