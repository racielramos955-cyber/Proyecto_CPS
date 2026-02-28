@echo off
echo ========================================
echo   NutriLife - Iniciar en Red Local
echo ========================================
echo.

cd /d "%~dp0"

REM Obtener IP local
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /i "IPv4" ^| findstr /v "192.168.106 192.168.35"') do (
    set IP_LOCAL=%%a
    goto :found
)
:found
set IP_LOCAL=%IP_LOCAL:~1%

echo [1/2] Iniciando Backend...
start "NutriLife Backend - Red Local" powershell -ExecutionPolicy Bypass -File "%~dp0iniciar_backend_red_local.ps1"

timeout /t 5 /nobreak >nul

echo [2/2] Iniciando Frontend...
start "NutriLife Frontend - Red Local" powershell -ExecutionPolicy Bypass -File "%~dp0iniciar_frontend_red_local.ps1"

echo.
echo ========================================
echo   Servicios Iniciados
echo ========================================
echo.
echo   Desde esta PC:
echo     Frontend: http://localhost:8000
echo     Backend:  http://localhost:5000
echo.
echo   Desde otros dispositivos (Red Local):
if not "%IP_LOCAL%"=="" (
    echo     Frontend: http://%IP_LOCAL%:8000
    echo     Backend:  http://%IP_LOCAL%:5000
) else (
    echo     IP no detectada. Ejecuta: ipconfig
    echo     Busca tu IPv4 y usa: http://TU_IP:8000
)
echo.
echo   Presiona cualquier tecla para cerrar...
pause >nul

