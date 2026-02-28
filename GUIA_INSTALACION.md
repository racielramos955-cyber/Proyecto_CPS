# 🚀 Guía Completa de Instalación - NutriLife AI + Web3

Esta guía te ayudará a instalar y configurar el proyecto correctamente en tu máquina.

---

## 📋 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- **Python 3.8 o superior** (recomendado 3.9 o 3.10)
- **Git** (para clonar el repositorio si es necesario)
- **Navegador moderno** (Chrome, Firefox, Edge)

### Verificar Python

Abre PowerShell y ejecuta:

```powershell
python --version
```

Deberías ver algo como: `Python 3.9.x` o superior.

---

## 🔧 Paso 1: Configurar Entorno Virtual

Un entorno virtual aísla las dependencias del proyecto. **Es muy recomendable usarlo.**

### Crear el entorno virtual

```powershell
# Navega a la carpeta del proyecto
cd "C:\Proyecto IA\IBM_Inteligente"

# Crea el entorno virtual
python -m venv .venv
```

### Activar el entorno virtual

```powershell
# En PowerShell:
.venv\Scripts\Activate.ps1

# Si tienes problemas de permisos, ejecuta primero:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**✅ Verificación:** Deberías ver `(.venv)` al inicio de tu línea de comando.

---

## 📦 Paso 2: Instalar Dependencias

Con el entorno virtual activado, instala todas las dependencias:

```powershell
# Asegúrate de que el .venv esté activado (debe aparecer (.venv) al inicio)
pip install --upgrade pip

# Instala todas las dependencias
pip install -r requirements.txt
```

**⏱️ Nota:** TensorFlow es grande (~500MB), puede tardar varios minutos.

### Verificar instalación

```powershell
python -c "import flask; import tensorflow; import flask_cors; print('✅ Todas las dependencias instaladas correctamente')"
```

---

## 🔐 Paso 3: Configurar Credenciales

El proyecto necesita archivos de configuración con tus credenciales.

### 3.1 Configurar Backend (.env)

Copia el archivo de credenciales al backend:

```powershell
# Copiar backend.env a backend/.env
Copy-Item credenciales\backend.env backend\.env
```

**Verificar:** Asegúrate de que existe `backend\.env` y contiene tu `PINATA_JWT`.

### 3.2 Configurar Frontend (Contrato Blockchain)

Copia los archivos de configuración del contrato:

```powershell
# Copiar contract-config.js
Copy-Item credenciales\contract-config.js frontend\js\contract-config.js

# Copiar NutriLifeABI.json
Copy-Item credenciales\NutriLifeABI.json frontend\js\NutriLifeABI.json
```

**✅ Verificación:** Verifica que estos archivos existen:
- `backend\.env`
- `frontend\js\contract-config.js`
- `frontend\js\NutriLifeABI.json`

---

## 🚀 Paso 4: Iniciar la Aplicación

Tienes dos opciones para iniciar la aplicación:

### Opción A: Script Automático (Recomendado)

```powershell
# Doble clic en el archivo o ejecuta:
.\iniciar_todo.bat
```

Este script:
- Activa el entorno virtual automáticamente
- Inicia el backend en http://localhost:5000
- Inicia el frontend en http://localhost:8000

### Opción B: Manual (Dos Terminales)

**Terminal 1 - Backend:**

```powershell
# Activa el entorno virtual
.venv\Scripts\Activate.ps1

# Inicia el backend
python backend/app.py
```

Deberías ver:
```
🚀 Iniciando NutriLife Backend API
📡 Servidor corriendo en: http://localhost:5000
```

**Terminal 2 - Frontend:**

```powershell
# Navega a la carpeta frontend
cd frontend

# Inicia el servidor HTTP
python -m http.server 8000
```

Deberías ver:
```
Serving HTTP on :: port 8000 (http://[::]:8000/) ...
```

---

## 🌐 Paso 5: Abrir la Aplicación

Abre tu navegador y ve a:

```
http://localhost:8000
```

---

## ✅ Verificar que Todo Funciona

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

### 2. Probar Funcionalidades

1. **Calculadora IMC:**
   - Ingresa peso y altura
   - Haz clic en "Calcular mi IMC"
   - Deberías ver recomendaciones

2. **Analizar Comida:**
   - Sube una imagen de comida
   - Haz clic en "🔍 Analizar Comida"
   - Deberías ver el resultado y un cuadro azul con información de IPFS

3. **Chatbot NutriBot:**
   - Haz una pregunta sobre nutrición
   - Deberías recibir una respuesta

---

## ⚠️ Solución de Problemas Comunes

### Error: "No module named 'flask'"

**Solución:**
```powershell
# Asegúrate de que el .venv esté activado
.venv\Scripts\Activate.ps1

# Reinstala las dependencias
pip install -r requirements.txt
```

### Error: "PINATA_JWT no configurado"

**Solución:**
```powershell
# Verifica que el archivo existe
Test-Path backend\.env

# Si no existe, cópialo:
Copy-Item credenciales\backend.env backend\.env
```

### Error: "El puerto 5000 ya está en uso"

**Solución:**
- Cierra otras aplicaciones que usen el puerto 5000
- O cambia el puerto en `backend/app.py` (línea final)

### Error: "El puerto 8000 ya está en uso"

**Solución:**
- Cierra otras aplicaciones que usen el puerto 8000
- O usa otro puerto: `python -m http.server 8080`

### El backend no inicia

**Verifica:**
1. ¿Está activado el entorno virtual? (debe aparecer `(.venv)`)
2. ¿Están instaladas las dependencias? (`pip list`)
3. ¿Existe `backend\.env`?

### El frontend no carga

**Verifica:**
1. ¿Está corriendo el servidor HTTP? (`python -m http.server 8000`)
2. ¿Está corriendo el backend? (http://localhost:5000)
3. ¿Abriste `http://localhost:8000` (no `file:///`)?

---

## 📚 Estructura de Archivos Importantes

```
IBM_Inteligente/
├── backend/
│   ├── app.py              # Servidor Flask principal
│   ├── .env                # ⚠️ Credenciales (no subir a GitHub)
│   ├── routes/             # Endpoints de la API
│   └── services/           # Servicios (IA, IPFS, etc.)
├── frontend/
│   ├── index.html          # Página principal
│   └── js/
│       ├── contract-config.js  # ⚠️ Configuración blockchain
│       └── NutriLifeABI.json   # ⚠️ ABI del contrato
├── credenciales/           # ⚠️ Carpeta con credenciales (no subir)
│   ├── backend.env
│   ├── contract-config.js
│   └── NutriLifeABI.json
├── modelos/                # Modelos de IA entrenados
├── requirements.txt        # Dependencias del proyecto
└── iniciar_todo.bat        # Script para iniciar todo
```

---

## 🔒 Seguridad

**⚠️ IMPORTANTE:** Nunca subas a GitHub:
- `backend\.env`
- `frontend\js\contract-config.js` (si contiene claves privadas)
- `credenciales\` (toda la carpeta)

Estos archivos contienen información sensible y deben mantenerse privados.

---

## 📝 Resumen de Comandos Rápidos

```powershell
# 1. Activar entorno virtual
.venv\Scripts\Activate.ps1

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Configurar credenciales
Copy-Item credenciales\backend.env backend\.env
Copy-Item credenciales\contract-config.js frontend\js\contract-config.js
Copy-Item credenciales\NutriLifeABI.json frontend\js\NutriLifeABI.json

# 4. Iniciar backend
python backend/app.py

# 5. Iniciar frontend (en otra terminal)
cd frontend
python -m http.server 8000
```

---

## 🎯 Próximos Pasos

Una vez que todo esté funcionando:

1. **Explora la documentación:** Revisa `documentacion/` para entender mejor el proyecto
2. **Prueba todas las funcionalidades:** IMC, análisis de imágenes, chatbot
3. **Revisa el código:** Entiende cómo funciona cada parte
4. **Personaliza:** Ajusta el proyecto según tus necesidades

---

## 📧 Soporte

Si tienes problemas:

1. Revisa la documentación en `documentacion/`
2. Consulta `frontend/SOLUCION_ERRORES.md`
3. Verifica que todos los pasos de esta guía se hayan completado correctamente

---

**¡Listo! Tu proyecto debería estar funcionando correctamente.** 🎉

