"""
Script para reorganizar y consolidar todas las imágenes de entrenamiento y validación
en una estructura única y organizada.

Este script:
1. Consolida todas las imágenes de entrenamiento en entrenamiento/
2. Consolida todas las imágenes de validación en validacion/
3. Detecta y evita duplicados
4. Genera un reporte de la reorganización
"""

import os
import shutil
from pathlib import Path
from collections import defaultdict
import hashlib

def calcular_hash_archivo(ruta_archivo):
    """Calcula el hash MD5 de un archivo para detectar duplicados."""
    hash_md5 = hashlib.md5()
    try:
        with open(ruta_archivo, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception as e:
        print(f"Error calculando hash de {ruta_archivo}: {e}")
        return None

def obtener_archivos_imagen(carpeta):
    """Obtiene todos los archivos de imagen de una carpeta."""
    extensiones = ('.jpg', '.jpeg', '.png', '.bmp', '.JPG', '.JPEG', '.PNG', '.BMP')
    archivos = []
    if os.path.exists(carpeta):
        for archivo in os.listdir(carpeta):
            if archivo.lower().endswith(extensiones):
                archivos.append(os.path.join(carpeta, archivo))
    return archivos

def crear_estructura_destino():
    """Crea la estructura de carpetas destino si no existe."""
    carpetas_destino = [
        'entrenamiento/Exceso_porcion',
        'entrenamiento/Porcion_correcta',
        'validacion/Exceso_porcion',
        'validacion/Porcion_correcta',
    ]
    
    for carpeta in carpetas_destino:
        os.makedirs(carpeta, exist_ok=True)
        print(f"[OK] Carpeta creada/verificada: {carpeta}")

def consolidar_imagenes():
    """Consolida todas las imágenes en la estructura final."""
    
    print("\n" + "=" * 70)
    print("REORGANIZACIÓN Y CONSOLIDACIÓN DE DATASET")
    print("=" * 70)
    
    # Crear estructura destino
    crear_estructura_destino()
    
    # Mapeo de fuentes a destino
    mapeo_consolidacion = {
        # ENTRENAMIENTO - Exceso de porción
        'entrenamiento/Exceso_porcion': 'entrenamiento/Exceso_porcion',
        'entrenamiento/Pruebas-ensambladas/Entrenamiento_Excesoporcion': 'entrenamiento/Exceso_porcion',
        'entrenamiento/Pruebas-ensambladas/Entrnamiento_Excesoporcion': 'entrenamiento/Exceso_porcion',  # Por si hay otro typo
        
        # ENTRENAMIENTO - Porción correcta
        'entrenamiento/Porcion_correcta': 'entrenamiento/Porcion_correcta',
        'entrenamiento/Pruebas-ensambladas/Entrenamiento_Porcioncorrecta': 'entrenamiento/Porcion_correcta',
        'entrenamiento/Pruebas-ensambladas/Entrnamiento_Porcioncorrecta': 'entrenamiento/Porcion_correcta',  # Tolerar typo
        
        # VALIDACIÓN - Exceso de porción
        'validacion/Exceso_porcion': 'validacion/Exceso_porcion',
        'validacion/Porcionexceso': 'validacion/Exceso_porcion',  # Nombre legacy
        'entrenamiento/Pruebas-ensambladas/Validacion_Excesoporcion': 'validacion/Exceso_porcion',
        
        # VALIDACIÓN - Porción correcta
        'validacion/Porcion_correcta': 'validacion/Porcion_correcta',
        'validacion/Porcioncorrecta': 'validacion/Porcion_correcta',  # Nombre legacy
        'entrenamiento/Pruebas-ensambladas/Validacion_Porcioncorrecta': 'validacion/Porcion_correcta',
    }
    
    # Estadísticas
    estadisticas = defaultdict(lambda: {'copiados': 0, 'duplicados': 0, 'errores': 0})
    archivos_hash = {}  # Para detectar duplicados
    
    print("\n[INFO] Iniciando consolidacion de imagenes...\n")
    
    for carpeta_origen, carpeta_destino in mapeo_consolidacion.items():
        if not os.path.exists(carpeta_origen):
            print(f"[ADVERTENCIA] Carpeta no encontrada (omitiendo): {carpeta_origen}")
            continue
        
        archivos = obtener_archivos_imagen(carpeta_origen)
        print(f"[CARPETA] {carpeta_origen} -> {carpeta_destino}")
        print(f"   Encontradas {len(archivos)} imágenes")
        
        for archivo_origen in archivos:
            nombre_archivo = os.path.basename(archivo_origen)
            archivo_destino = os.path.join(carpeta_destino, nombre_archivo)
            
            # Si ya existe un archivo con el mismo nombre, verificar si es duplicado
            if os.path.exists(archivo_destino):
                # Calcular hash de ambos archivos
                hash_origen = calcular_hash_archivo(archivo_origen)
                hash_destino = calcular_hash_archivo(archivo_destino)
                
                if hash_origen and hash_destino and hash_origen == hash_destino:
                    # Es un duplicado exacto, omitir
                    estadisticas[carpeta_destino]['duplicados'] += 1
                    print(f"   [DUPLICADO] Duplicado omitido: {nombre_archivo}")
                    continue
                else:
                    # Mismo nombre pero diferente contenido, renombrar
                    base, ext = os.path.splitext(nombre_archivo)
                    contador = 1
                    nuevo_nombre = f"{base}_dup{contador}{ext}"
                    archivo_destino = os.path.join(carpeta_destino, nuevo_nombre)
                    while os.path.exists(archivo_destino):
                        contador += 1
                        nuevo_nombre = f"{base}_dup{contador}{ext}"
                        archivo_destino = os.path.join(carpeta_destino, nuevo_nombre)
                    print(f"   [RENOMBRAR] Renombrado para evitar conflicto: {nuevo_nombre}")
            
            # Verificar duplicados por hash
            hash_archivo = calcular_hash_archivo(archivo_origen)
            if hash_archivo:
                if hash_archivo in archivos_hash:
                    # Ya copiamos este archivo antes, omitir
                    estadisticas[carpeta_destino]['duplicados'] += 1
                    print(f"   [DUPLICADO] Duplicado por hash omitido: {nombre_archivo}")
                    continue
                archivos_hash[hash_archivo] = archivo_destino
            
            # Copiar archivo
            try:
                shutil.copy2(archivo_origen, archivo_destino)
                estadisticas[carpeta_destino]['copiados'] += 1
            except Exception as e:
                estadisticas[carpeta_destino]['errores'] += 1
                print(f"   [ERROR] Error copiando {nombre_archivo}: {e}")
        
        print(f"   [OK] Copiados: {estadisticas[carpeta_destino]['copiados']}, "
              f"Duplicados: {estadisticas[carpeta_destino]['duplicados']}, "
              f"Errores: {estadisticas[carpeta_destino]['errores']}\n")
    
    # Reporte final
    print("\n" + "=" * 70)
    print("REPORTE FINAL DE CONSOLIDACIÓN")
    print("=" * 70)
    
    total_copiados = 0
    total_duplicados = 0
    total_errores = 0
    
    for carpeta, stats in estadisticas.items():
        total_imagenes = len(obtener_archivos_imagen(carpeta))
        print(f"\n[CARPETA] {carpeta}:")
        print(f"   [OK] Imagenes copiadas: {stats['copiados']}")
        print(f"   [DUPLICADOS] Duplicados omitidos: {stats['duplicados']}")
        print(f"   [ERRORES] Errores: {stats['errores']}")
        print(f"   [TOTAL] Total final en carpeta: {total_imagenes} imagenes")
        
        total_copiados += stats['copiados']
        total_duplicados += stats['duplicados']
        total_errores += stats['errores']
    
    print("\n" + "-" * 70)
    print(f"TOTALES:")
    print(f"   [OK] Imagenes consolidadas: {total_copiados}")
    print(f"   [DUPLICADOS] Duplicados detectados: {total_duplicados}")
    print(f"   [ERRORES] Errores: {total_errores}")
    print("=" * 70)
    
    # Contar imágenes finales
    print("\n[RESUMEN] RESUMEN DE IMAGENES FINALES:")
    print("-" * 70)
    for carpeta in ['entrenamiento/Exceso_porcion', 'entrenamiento/Porcion_correcta',
                    'validacion/Exceso_porcion', 'validacion/Porcion_correcta']:
        total = len(obtener_archivos_imagen(carpeta))
        tipo = "ENTRENAMIENTO" if "entrenamiento" in carpeta else "VALIDACIÓN"
        clase = "Exceso" if "Exceso" in carpeta else "Porción Correcta"
        print(f"   {tipo} - {clase}: {total} imágenes")
    
    print("\n[OK] CONSOLIDACION COMPLETADA")
    print("=" * 70)
    print("\n[INFO] Proximo paso: Ejecuta el preprocesamiento y entrenamiento")
    print("   python scripts/preprocesamiento_mejorado.py")
    print("   python scripts/entrenar_modelo_mejorado.py")

if __name__ == "__main__":
    # Cambiar al directorio del proyecto
    script_dir = os.path.dirname(os.path.abspath(__file__))
    proyecto_dir = os.path.dirname(script_dir)
    os.chdir(proyecto_dir)
    
    print(f"Directorio de trabajo: {os.getcwd()}")
    
    consolidar_imagenes()
