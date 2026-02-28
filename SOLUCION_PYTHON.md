# 🔧 Solución: Python no encontrado

## ⚠️ Problema Detectado

El script de configuración no pudo encontrar Python en tu sistema. Esto significa que:
- Python no está instalado, O
- Python está instalado pero no está en el PATH del sistema

## ✅ Solución 1: Verificar si Python está instalado

Abre PowerShell y ejecuta estos comandos para buscar Python:

```powershell
# Buscar Python en ubicaciones comunes
Get-ChildItem -Path "C:\Python*" -ErrorAction SilentlyContinue
Get-ChildItem -Path "$env:LOCALAPPDATA\Programs\Python" -ErrorAction SilentlyContinue
Get-ChildItem -Path "C:\Program Files\Python*" -ErrorAction SilentlyContinue
Get-ChildItem -Path "$env:USERPROFILE\AppData\Local\Programs\Python" -ErrorAction SilentlyContinue
```

Si encuentras Python, anota la ruta completa (ejemplo: `C:\Python39\python.exe`)

## ✅ Solución 2: Instalar Python (si no está instalado)

### Opción A: Desde python.org (Recomendado)

1. Ve a: https://www.python.org/downloads/
2. Descarga Python 3.9 o 3.10 (NO 3.11 o superior, puede tener problemas con TensorFlow)
3. Durante la instalación, **Marca la casilla "Add Python to PATH"**
4. Instala normalmente

### Opción B: Desde Microsoft Store

1. Abre Microsoft Store
2. Busca "Python 3.9" o "Python 3.10"
3. Instala Python
4. Nota: Puede que necesites agregar Python al PATH manualmente

## ✅ Solución 3: Agregar Python al PATH (si ya está instalado)

Si Python está instalado pero no está en el PATH:

### Paso 1: Encontrar la ruta de Python

Ejecuta en PowerShell:
```powershell
# Buscar python.exe
Get-ChildItem -Path C:\ -Filter python.exe -Recurse -ErrorAction SilentlyContinue | Select-Object FullName
```

### Paso 2: Agregar al PATH

1. Presiona `Win + X` y selecciona "Sistema"
2. Haz clic en "Configuración avanzada del sistema"
3. Haz clic en "Variables de entorno"
4. En "Variables del sistema", busca "Path" y haz clic en "Editar"
5. Haz clic en "Nuevo" y agrega la ruta donde está Python (ejemplo: `C:\Python39`)
6. También agrega la ruta a Scripts (ejemplo: `C:\Python39\Scripts`)
7. Haz clic en "Aceptar" en todas las ventanas
8. **Cierra y vuelve a abrir PowerShell** para que los cambios surtan efecto

## ✅ Solución 4: Usar Python directamente con ruta completa

Si Python está instalado pero no quieres modificar el PATH, puedes usar la ruta completa:

```powershell
# Reemplaza C:\Python39\python.exe con tu ruta real
C:\Python39\python.exe --version

# Crear entorno virtual
C:\Python39\python.exe -m venv .venv

# Activar entorno virtual
.venv\Scripts\Activate.ps1

# Instalar dependencias
pip install -r requirements.txt
```

## 🧪 Verificar que Python funciona

Después de instalar o configurar Python, verifica:

```powershell
python --version
```

Deberías ver algo como: `Python 3.9.x` o `Python 3.10.x`

## 🚀 Continuar con la instalación

Una vez que Python esté funcionando, puedes:

### Opción A: Ejecutar el script automático nuevamente

```powershell
.\configurar_proyecto.ps1
```

### Opción B: Instalación manual paso a paso

```powershell
# 1. Crear entorno virtual
python -m venv .venv

# 2. Activar entorno virtual
.venv\Scripts\Activate.ps1

# 3. Actualizar pip
python -m pip install --upgrade pip

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Configurar credenciales
Copy-Item credenciales\backend.env backend\.env
Copy-Item credenciales\contract-config.js frontend\js\contract-config.js
Copy-Item credenciales\NutriLifeABI.json frontend\js\NutriLifeABI.json

# 6. Verificar instalación
python verificar_instalacion.py
```

## 📝 Notas Importantes

- **Python 3.8, 3.9 o 3.10** son las versiones recomendadas
- **Python 3.11+** puede tener problemas de compatibilidad con TensorFlow
- Asegúrate de marcar "Add Python to PATH" durante la instalación
- Después de modificar el PATH, **cierra y vuelve a abrir PowerShell**

## ❓ ¿Necesitas ayuda?

Si Python está instalado pero no lo encuentras, comparte:
1. La versión de Windows que usas
2. Cómo instalaste Python (desde python.org, Microsoft Store, Anaconda, etc.)
3. Cualquier mensaje de error que veas

---

**Una vez que Python esté configurado, vuelve a ejecutar el script de configuración.**

