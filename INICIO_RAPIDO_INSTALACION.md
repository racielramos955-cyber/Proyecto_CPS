# ⚡ Inicio Rápido - Instalación

## 🎯 Opción 1: Configuración Automática (Recomendado)

Ejecuta este comando en PowerShell desde la carpeta del proyecto:

```powershell
.\configurar_proyecto.ps1
```

Este script:
- ✅ Verifica Python
- ✅ Crea el entorno virtual (.venv)
- ✅ Instala todas las dependencias
- ✅ Configura las credenciales automáticamente

---

## 🎯 Opción 2: Configuración Manual

### Paso 1: Crear y activar entorno virtual

```powershell
# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual
.venv\Scripts\Activate.ps1
```

### Paso 2: Instalar dependencias

```powershell
# Asegúrate de que el .venv esté activado (debe aparecer (.venv))
pip install --upgrade pip
pip install -r requirements.txt
```

### Paso 3: Configurar credenciales

```powershell
# Copiar credenciales del backend
Copy-Item credenciales\backend.env backend\.env

# Copiar configuración del frontend
Copy-Item credenciales\contract-config.js frontend\js\contract-config.js
Copy-Item credenciales\NutriLifeABI.json frontend\js\NutriLifeABI.json
```

### Paso 4: Verificar instalación

```powershell
python verificar_instalacion.py
```

---

## 🚀 Iniciar la Aplicación

### Opción A: Script automático

```powershell
.\iniciar_todo.bat
```

### Opción B: Manual (dos terminales)

**Terminal 1 - Backend:**
```powershell
.venv\Scripts\Activate.ps1
python backend\app.py
```

**Terminal 2 - Frontend:**
```powershell
cd frontend
python -m http.server 8000
```

---

## 🌐 Abrir en el Navegador

```
http://localhost:8000
```

---

## ✅ Verificar que Funciona

1. **Backend:** Abre http://localhost:5000 - Deberías ver un JSON con el estado
2. **Frontend:** Abre http://localhost:8000 - Deberías ver la aplicación
3. **Prueba:** Sube una imagen de comida y analízala

---

## ⚠️ Problemas Comunes

### "No module named 'flask'"
```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### "PINATA_JWT no configurado"
```powershell
Copy-Item credenciales\backend.env backend\.env
```

### "El puerto 5000/8000 ya está en uso"
Cierra otras aplicaciones que usen esos puertos o cambia el puerto en el código.

---

## 📚 Más Información

- **Guía completa:** `GUIA_INSTALACION.md`
- **Documentación:** `documentacion/`
- **Solución de errores:** `frontend/SOLUCION_ERRORES.md`

---

**¡Listo! Tu proyecto debería estar funcionando.** 🎉

