# 🔧 Solución de Errores al Iniciar la Aplicación

## ⚠️ Errores Comunes y Soluciones

### Error 1: "No se encontró el módulo 'flask'"

**Síntomas:**
```
ModuleNotFoundError: No module named 'flask'
```

**Solución:**
```powershell
# 1. Activa el entorno virtual
.venv\Scripts\Activate.ps1

# 2. Instala las dependencias
pip install -r requirements.txt
```

---

### Error 2: "El puerto 5000 ya está en uso"

**Síntomas:**
```
OSError: [Errno 48] Address already in use
```

**Solución:**

**Opción A: Cerrar el proceso que usa el puerto**
```powershell
# Encontrar el proceso que usa el puerto 5000
netstat -ano | findstr :5000

# Matar el proceso (reemplaza PID con el número que aparezca)
taskkill /PID <PID> /F
```

**Opción B: Cambiar el puerto**
Edita `backend/app.py` línea 60:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Cambiar a 5001
```

---

### Error 3: "El puerto 8000 ya está en uso"

**Síntomas:**
```
OSError: [Errno 48] Address already in use
```

**Solución:**

**Opción A: Cerrar el proceso**
```powershell
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

**Opción B: Usar otro puerto**
```powershell
cd frontend
python -m http.server 8080
```
Luego abre: http://localhost:8080

---

### Error 4: "PINATA_JWT no configurado"

**Síntomas:**
```
Error: PINATA_JWT no configurado
```

**Solución:**
```powershell
# Copiar el archivo de credenciales
Copy-Item credenciales\backend.env backend\.env

# Verificar que se copió correctamente
Test-Path backend\.env
```

---

### Error 5: "No se puede cargar el modelo"

**Síntomas:**
```
FileNotFoundError: No se encontró el modelo
```

**Solución:**
Verifica que existan los modelos:
```powershell
Test-Path modelos\modelo_porciones.keras
Test-Path modelos\mejor_modelo.h5
```

Si no existen, necesitas entrenar el modelo primero o descargarlo.

---

### Error 6: "Python no se reconoce como comando"

**Síntomas:**
```
'python' no se reconoce como un comando interno o externo
```

**Solución:**

**Si usas Python de QGIS:**
```powershell
# Usa la ruta completa
& "C:\Program Files\QGIS 3.44.5\apps\Python312\python.exe" backend\app.py
```

**O agrega Python al PATH:**
1. Busca la ubicación de Python
2. Agrega la carpeta al PATH del sistema
3. Reinicia PowerShell

---

### Error 7: "Error al activar el entorno virtual"

**Síntomas:**
```
.venv\Scripts\Activate.ps1 : No se puede cargar
```

**Solución:**
```powershell
# Cambiar la política de ejecución
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Luego intenta de nuevo
.venv\Scripts\Activate.ps1
```

---

## ✅ Comandos Correctos para Iniciar

### Backend (Terminal 1):
```powershell
# Navegar al proyecto
cd "C:\Proyecto IA\IBM_Inteligente"

# Activar entorno virtual
.venv\Scripts\Activate.ps1

# Iniciar backend
python backend\app.py
```

### Frontend (Terminal 2):
```powershell
# Navegar al proyecto
cd "C:\Proyecto IA\IBM_Inteligente"

# Ir a la carpeta frontend
cd frontend

# Iniciar servidor HTTP
python -m http.server 8000
```

**NOTA:** Observa que hay un espacio entre `cd frontend` y `python`. El comando correcto es:
- ✅ `cd frontend` (luego Enter, luego) `python -m http.server 8000`
- ❌ `cd frontendpython` (sin espacio - esto es incorrecto)

---

## 🚀 Scripts Automáticos (Recomendado)

He creado scripts que manejan estos errores automáticamente:

### Opción 1: Iniciar todo automáticamente
```powershell
.\iniciar_todo_corregido.bat
```

### Opción 2: Iniciar por separado

**Backend:**
```powershell
.\iniciar_backend.ps1
```

**Frontend:**
```powershell
.\iniciar_frontend.ps1
```

---

## 🔍 Verificar que Todo Funciona

### 1. Verificar Backend
Abre en el navegador: http://localhost:5000

Deberías ver:
```json
{
  "message": "NutriLife AI + Web3 API",
  "version": "1.0.0",
  "status": "running"
}
```

### 2. Verificar Frontend
Abre en el navegador: http://localhost:8000

Deberías ver la interfaz de la aplicación.

### 3. Verificar Endpoint de Salud
Abre: http://localhost:5000/api/health

Deberías ver el estado del servidor y si el modelo está cargado.

---

## 📝 Checklist de Verificación

Antes de iniciar, verifica:

- [ ] Entorno virtual creado (`.venv` existe)
- [ ] Dependencias instaladas (`pip list` muestra flask, tensorflow, etc.)
- [ ] `backend/.env` existe y tiene `PINATA_JWT`
- [ ] `frontend/js/contract-config.js` existe
- [ ] `frontend/js/NutriLifeABI.json` existe
- [ ] Modelos de IA existen (`modelos/modelo_porciones.keras`)
- [ ] Puertos 5000 y 8000 no están en uso

---

## 🆘 Si Nada Funciona

1. **Ejecuta el script de verificación:**
```powershell
.venv\Scripts\Activate.ps1
python verificar_instalacion.py
```

2. **Reinstala las dependencias:**
```powershell
.venv\Scripts\Activate.ps1
pip install --force-reinstall -r requirements.txt
```

3. **Reconfigura las credenciales:**
```powershell
Copy-Item credenciales\backend.env backend\.env -Force
Copy-Item credenciales\contract-config.js frontend\js\contract-config.js -Force
Copy-Item credenciales\NutriLifeABI.json frontend\js\NutriLifeABI.json -Force
```

---

**¿Sigue sin funcionar?** Comparte el mensaje de error completo y te ayudo a solucionarlo.

