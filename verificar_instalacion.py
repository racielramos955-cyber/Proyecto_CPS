"""
Script para verificar qué está instalado y dónde
Incluye verificación de dependencias, credenciales y archivos de configuración
"""

import sys
import os
from pathlib import Path

# Configurar encoding para evitar problemas con emojis en Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

print("=" * 60)
print("VERIFICACION COMPLETA DE INSTALACION")
print("=" * 60)

# Obtener directorio base del proyecto
base_dir = Path(__file__).parent

print(f"\n[PYTHON] Ejecutable: {sys.executable}")
print(f"[PYTHON] Usando .venv: {'.venv' in sys.executable}")

# Verificar archivos de configuracion
print("\n[CONFIG] Verificando archivos de configuracion...\n")

archivos_config = {
    'backend/.env': 'Archivo de credenciales del backend (PINATA_JWT)',
    'frontend/js/contract-config.js': 'Configuración del contrato blockchain',
    'frontend/js/NutriLifeABI.json': 'ABI del contrato inteligente',
    'modelos/modelo_porciones.keras': 'Modelo de IA entrenado',
    'modelos/mejor_modelo.h5': 'Modelo alternativo (opcional)'
}

for archivo, descripcion in archivos_config.items():
    ruta = base_dir / archivo
    if ruta.exists():
        tamaño = ruta.stat().st_size
        print(f"[OK] {archivo:35} - {descripcion}")
        print(f"     Tamano: {tamaño:,} bytes")
    else:
        print(f"[ERROR] {archivo:35} - NO ENCONTRADO")
        print(f"   {descripcion}")
    print()

# Verificar credenciales en backend/.env
print("\n[CREDENCIALES] Verificando credenciales...\n")
env_file = base_dir / 'backend' / '.env'
if env_file.exists():
    try:
        with open(env_file, 'r') as f:
            contenido = f.read()
            if 'PINATA_JWT' in contenido:
                jwt_length = len([line for line in contenido.split('\n') if 'PINATA_JWT' in line and '=' in line])
                if jwt_length > 0:
                    print("[OK] PINATA_JWT encontrado en backend/.env")
                else:
                    print("[ADVERTENCIA] backend/.env existe pero PINATA_JWT no esta configurado")
            else:
                print("[ERROR] backend/.env existe pero no contiene PINATA_JWT")
    except Exception as e:
        print(f"[ADVERTENCIA] Error al leer backend/.env: {e}")
else:
    print("[ERROR] backend/.env NO EXISTE")
    print("   Solución: Copy-Item credenciales\\backend.env backend\\.env")

print()

# Verificar dependencias
print("\n📦 Verificando dependencias...\n")

dependencias = [
    'flask',
    'flask_cors',
    'tensorflow',
    'numpy',
    'cv2',
    'PIL',
    'dotenv'
]

for dep in dependencias:
    try:
        if dep == 'flask_cors':
            module = __import__('flask_cors')
        elif dep == 'cv2':
            module = __import__('cv2')
        elif dep == 'PIL':
            module = __import__('PIL')
        elif dep == 'dotenv':
            module = __import__('dotenv')
        else:
            module = __import__(dep)
        
        # Obtener versión si existe
        version = getattr(module, '__version__', 'instalado')
        ubicacion = os.path.dirname(module.__file__)
        
        print(f"[OK] {dep:15} - Version: {version}")
        if '.venv' in ubicacion:
            print(f"     Ubicacion: {ubicacion} (en .venv)")
        else:
            print(f"     Ubicacion: {ubicacion}")
    except ImportError:
        print(f"[ERROR] {dep:15} - NO INSTALADO")
    print()

# Resumen
print("=" * 60)
print("\n📋 RESUMEN")
print("=" * 60)

errores = []
if not (base_dir / 'backend' / '.env').exists():
    errores.append("❌ Falta: backend/.env (copia desde credenciales/backend.env)")
if not (base_dir / 'frontend' / 'js' / 'contract-config.js').exists():
    errores.append("❌ Falta: frontend/js/contract-config.js")
if not (base_dir / 'frontend' / 'js' / 'NutriLifeABI.json').exists():
    errores.append("❌ Falta: frontend/js/NutriLifeABI.json")

if errores:
    print("\n[ADVERTENCIA] PROBLEMAS ENCONTRADOS:")
    for error in errores:
        print(f"   {error}")
    print("\n[SOLUCION] Solucion rapida:")
    print("   Copy-Item credenciales\\backend.env backend\\.env")
    print("   Copy-Item credenciales\\contract-config.js frontend\\js\\contract-config.js")
    print("   Copy-Item credenciales\\NutriLifeABI.json frontend\\js\\NutriLifeABI.json")
else:
    print("\n[OK] Todos los archivos de configuracion estan presentes")

print("\n[AYUDA] Si alguna dependencia muestra [ERROR], instalala con:")
print("   pip install -r requirements.txt")
print("\n[AYUDA] Si estas en .venv y no se instala ahi:")
print("   .venv\\Scripts\\Activate.ps1")
print("   pip install -r requirements.txt")
print("=" * 60)

