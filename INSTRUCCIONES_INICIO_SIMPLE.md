# 🚀 Instrucciones Simples para Iniciar la Aplicación

## ✅ Método Más Fácil (Recomendado)

**Ejecuta este comando en PowerShell:**

```powershell
cd "C:\Proyecto IA\IBM_Inteligente"
.\iniciar_servicios.ps1
```

Este script:
- ✅ Inicia el backend automáticamente
- ✅ Inicia el frontend automáticamente
- ✅ Abre el navegador en http://localhost:8000
- ✅ Todo en ventanas separadas

---

## 📋 Método Manual (Paso a Paso)

Si prefieres hacerlo manualmente, sigue estos pasos:

### Paso 1: Abrir Terminal 1 (Backend)

```powershell
# 1. Ir al proyecto
cd "C:\Proyecto IA\IBM_Inteligente"

# 2. Activar entorno virtual
.venv\Scripts\Activate.ps1

# 3. Iniciar backend
python backend\app.py
```

**Deberías ver:**
```
✅ Modelo cargado correctamente
🚀 Iniciando NutriLife Backend API
📡 Servidor corriendo en: http://localhost:5000
```

### Paso 2: Abrir Terminal 2 (Frontend)

**Abre una NUEVA ventana de PowerShell** y ejecuta:

```powershell
# 1. Ir al proyecto
cd "C:\Proyecto IA\IBM_Inteligente"

# 2. Ir a la carpeta frontend
cd frontend

# 3. Iniciar servidor HTTP
python -m http.server 8000
```

**Deberías ver:**
```
Serving HTTP on :: port 8000 (http://[::]:8000/) ...
```

### Paso 3: Abrir en el Navegador

Abre tu navegador y ve a:
```
http://localhost:8000
```

---

## 🔍 Verificar que Todo Funciona

### 1. Verificar Backend

Abre en el navegador: **http://localhost:5000**

Deberías ver:
```json
{
  "message": "NutriLife AI + Web3 API",
  "version": "1.0.0",
  "status": "running"
}
```

### 2. Verificar Frontend

Abre en el navegador: **http://localhost:8000**

Deberías ver la interfaz de la aplicación NutriLife.

### 3. Verificar Endpoint de Salud

Abre: **http://localhost:5000/api/health**

Deberías ver el estado del servidor.

---

## ⚠️ Problemas Comunes

### Problema 1: "No se puede activar el entorno virtual"

**Solución:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Problema 2: "ModuleNotFoundError"

**Solución:**
```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Problema 3: "El puerto 5000/8000 ya está en uso"

**Solución:**
```powershell
# Encontrar y cerrar el proceso
netstat -ano | findstr :5000
taskkill /PID <NUMERO> /F
```

### Problema 4: "Python no se reconoce"

**Solución:**
Si usas Python de QGIS, usa la ruta completa:
```powershell
& "C:\Program Files\QGIS 3.44.5\apps\Python312\python.exe" backend\app.py
```

---

## 📝 Checklist Rápido

Antes de iniciar, verifica:

- [ ] Estás en el directorio correcto: `C:\Proyecto IA\IBM_Inteligente`
- [ ] Existe `.venv` (entorno virtual)
- [ ] Existe `backend\app.py`
- [ ] Existe `frontend\index.html`
- [ ] Existe `backend\.env` (con PINATA_JWT)

---

## 🎯 Resumen de Comandos

**Iniciar todo automáticamente:**
```powershell
.\iniciar_servicios.ps1
```

**Iniciar manualmente (Backend):**
```powershell
.venv\Scripts\Activate.ps1
python backend\app.py
```

**Iniciar manualmente (Frontend):**
```powershell
cd frontend
python -m http.server 8000
```

---

## 🆘 Si Nada Funciona

1. **Verifica la instalación:**
```powershell
.venv\Scripts\Activate.ps1
python verificar_instalacion.py
```

2. **Reinstala dependencias:**
```powershell
.venv\Scripts\Activate.ps1
pip install --force-reinstall -r requirements.txt
```

3. **Verifica credenciales:**
```powershell
Test-Path backend\.env
Test-Path frontend\js\contract-config.js
```

---

**¡Listo! Tu aplicación debería estar funcionando.** 🎉

