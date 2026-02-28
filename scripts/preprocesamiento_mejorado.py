"""
Script mejorado de preprocesamiento de imagenes para el modelo de clasificaciÃ³n
de porciones de comida.

Este script combina imagenes de mÃºltiples fuentes:
- entrenamiento/ (dataset original)
- Pruebas-ensambladas/ (nuevo dataset expandido)

Mejora: Combina todos los datos para crear un dataset mÃ¡s robusto.
"""

import os
import numpy as np
from PIL import Image
import cv2
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import shutil

class PreprocesadorImagenesMejorado:
    """Clase mejorada para preprocesar imagenes de comida combinando mÃºltiples fuentes."""
    
    def __init__(self, img_size=(224, 224)):
        """
        Inicializa el preprocesador.
        
        Args:
            img_size: Tupla (ancho, alto) para redimensionar imagenes. Default: (224, 224)
        """
        self.img_size = img_size
        self.classes = ['Porcion_correcta', 'Exceso_porcion']
        self.class_labels = {0: 'Porcion_correcta', 1: 'Exceso_porcion'}
        self.label_to_int = {'Porcion_correcta': 0, 'Exceso_porcion': 1}
    
    def cargar_imagen(self, ruta_imagen):
        """
        Carga y preprocesa una imagen individual.
        
        Args:
            ruta_imagen: Ruta completa a la imagen
            
        Returns:
            numpy array: Imagen preprocesada normalizada (0-1)
        """
        try:
            # Cargar imagen
            img = cv2.imread(ruta_imagen)
            
            if img is None:
                print(f"Error: No se pudo cargar la imagen {ruta_imagen}")
                return None
            
            # Convertir BGR a RGB
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            
            # Redimensionar
            img = cv2.resize(img, self.img_size)
            
            # Normalizar a [0, 1]
            img = img.astype(np.float32) / 255.0
            
            return img
            
        except Exception as e:
            print(f"Error procesando {ruta_imagen}: {str(e)}")
            return None
    
    def cargar_imagenes_de_carpeta(self, carpeta, label, fuente=""):
        """
        Carga todas las imagenes de una carpeta especÃ­fica.
        
        Args:
            carpeta: Ruta a la carpeta
            label: Etiqueta numÃ©rica de la clase
            fuente: Nombre de la fuente (para logging)
            
        Returns:
            Lista de imagenes y etiquetas
        """
        X = []
        y = []
        
        if not os.path.exists(carpeta):
            print(f"  [ADVERTENCIA] No se encontro la carpeta {carpeta}")
            return X, y
        
        archivos = os.listdir(carpeta)
        archivos_imagen = [f for f in archivos if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp'))]
        
        print(f"  [CARPETA] {fuente}: Cargando {len(archivos_imagen)} imagenes de {carpeta}...")
        
        for archivo in archivos_imagen:
            ruta_completa = os.path.join(carpeta, archivo)
            img = self.cargar_imagen(ruta_completa)
            
            if img is not None:
                X.append(img)
                y.append(label)
            else:
                print(f"    [ADVERTENCIA] No se pudo cargar: {archivo}")
        
        return X, y
    
    def cargar_dataset_combinado(self):
        """
        Carga todas las imagenes de entrenamiento de mÃºltiples fuentes y las combina.
        
        Returns:
            X: Array numpy con las imagenes
            y: Array numpy con las etiquetas
        """
        X = []
        y = []
        
        print("\n" + "=" * 60)
        print("CARGANDO DATASET COMBINADO DE ENTRENAMIENTO")
        print("=" * 60)
        
        # Mapeo de clases a carpetas (estructura consolidada)
        mapeo_clases = {
            'Porcion_correcta': [
                ('entrenamiento/Porcion_correcta', 'Dataset Consolidado'),
            ],
            'Exceso_porcion': [
                ('entrenamiento/Exceso_porcion', 'Dataset Consolidado'),
            ]
        }
        
        for clase, carpetas in mapeo_clases.items():
            label = self.label_to_int[clase]
            print(f"\n[CLASE] Clase: {clase} (Label: {label})")
            
            for carpeta, fuente in carpetas:
                if os.path.exists(carpeta):
                    X_clase, y_clase = self.cargar_imagenes_de_carpeta(carpeta, label, fuente)
                    X.extend(X_clase)
                    y.extend(y_clase)
                else:
                    print(f"  [ADVERTENCIA] Carpeta no encontrada: {carpeta} (omitiendo)")
        
        X = np.array(X)
        y = np.array(y)
        
        print("\n" + "=" * 60)
        print("RESUMEN DEL DATASET COMBINADO")
        print("=" * 60)
        print(f"[OK] Total de imagenes cargadas: {len(X)}")
        print(f"[INFO] Forma de X: {X.shape}")
        
        # Contar por clase
        unique, counts = np.unique(y, return_counts=True)
        for label, count in zip(unique, counts):
            clase_nombre = self.class_labels[label]
            print(f"   - {clase_nombre}: {count} imagenes")
        
        # Verificar balance
        if len(counts) == 2:
            ratio = counts[0] / counts[1] if counts[1] > 0 else 0
            if 0.8 <= ratio <= 1.2:
                print("   [OK] Dataset balanceado")
            else:
                print(f"   [ADVERTENCIA] Dataset desbalanceado (ratio: {ratio:.2f})")
        
        return X, y
    
    def cargar_validacion_combinada(self):
        """
        Carga las imagenes de validacion de mÃºltiples fuentes.
        
        Returns:
            X_val: Array numpy con las imagenes de validacion
            y_val: Array numpy con las etiquetas de validacion
        """
        X_val = []
        y_val = []
        
        print("\n" + "=" * 60)
        print("CARGANDO DATASET COMBINADO DE VALIDACIÃ“N")
        print("=" * 60)
        
        # Mapeo de validacion usando estructura consolidada
        mapeo_validacion = {
            'Porcion_correcta': [
                ('validacion/Porcion_correcta', 'Dataset Consolidado'),
            ],
            'Exceso_porcion': [
                ('validacion/Exceso_porcion', 'Dataset Consolidado'),
            ]
        }
        
        for clase_nombre, carpetas in mapeo_validacion.items():
            label = self.label_to_int[clase_nombre]
            print(f"\n[CLASE] Clase: {clase_nombre} (Label: {label})")
            
            for carpeta, fuente in carpetas:
                if os.path.exists(carpeta):
                    X_clase, y_clase = self.cargar_imagenes_de_carpeta(carpeta, label, fuente)
                    X_val.extend(X_clase)
                    y_val.extend(y_clase)
                else:
                    print(f"  [ADVERTENCIA] Carpeta no encontrada: {carpeta} (omitiendo)")
        
        X_val = np.array(X_val) if len(X_val) > 0 else np.array([])
        y_val = np.array(y_val) if len(y_val) > 0 else np.array([])
        
        print("\n" + "=" * 60)
        print("RESUMEN DEL DATASET DE VALIDACIÃ“N")
        print("=" * 60)
        print(f"[OK] Total de imagenes de validacion: {len(X_val)}")
        if len(X_val) > 0:
            print(f"[INFO] Forma de X_val: {X_val.shape}")
            unique, counts = np.unique(y_val, return_counts=True)
            for label, count in zip(unique, counts):
                clase_nombre = self.class_labels[label]
                print(f"   - {clase_nombre}: {count} imagenes")
        
        return X_val, y_val
    
    def visualizar_imagenes(self, X, y, n_muestras=8, titulo='Muestras del Dataset'):
        """
        Visualiza algunas imagenes del dataset.
        
        Args:
            X: Array de imagenes
            y: Array de etiquetas
            n_muestras: NÃºmero de muestras por clase a visualizar
            titulo: TÃ­tulo del grÃ¡fico
        """
        os.makedirs('documentacion', exist_ok=True)
        
        fig, axes = plt.subplots(2, n_muestras, figsize=(20, 6))
        fig.suptitle(titulo, fontsize=16)
        
        for clase_idx, clase_nombre in self.class_labels.items():
            indices_clase = np.where(y == clase_idx)[0]
            
            if len(indices_clase) == 0:
                # Si no hay imagenes de esta clase, mostrar cuadros vacÃ­os
                for i in range(n_muestras):
                    axes[clase_idx, i].axis('off')
                continue
            
            # Tomar n_muestras aleatorias
            n_tomar = min(n_muestras, len(indices_clase))
            indices_muestra = np.random.choice(indices_clase, n_tomar, replace=False)
            
            for i in range(n_muestras):
                if i < len(indices_muestra):
                    idx = indices_muestra[i]
                    img = X[idx]
                    axes[clase_idx, i].imshow(img)
                    axes[clase_idx, i].set_title(f'{clase_nombre}\n(#{idx})', fontsize=10)
                else:
                    axes[clase_idx, i].axis('off')
                axes[clase_idx, i].axis('off')
        
        plt.tight_layout()
        plt.savefig('documentacion/muestras_dataset_mejorado.png', dpi=150, bbox_inches='tight')
        print(f"\n[OK] Imagen guardada en: documentacion/muestras_dataset_mejorado.png")
        plt.close()


if __name__ == "__main__":
    print("=" * 60)
    print("PREPROCESAMIENTO MEJORADO DE IMAGENES")
    print("Combinando datasets originales y nuevos")
    print("=" * 60)
    
    # Crear preprocesador
    preprocesador = PreprocesadorImagenesMejorado(img_size=(224, 224))
    
    # Cargar dataset de entrenamiento combinado
    print("\n[PASO 1] Cargando dataset de entrenamiento consolidado...")
    X_train, y_train = preprocesador.cargar_dataset_combinado()
    
    # Cargar dataset de validacion combinado
    print("\n[PASO 2] Cargando dataset de validacion consolidado...")
    X_val, y_val = preprocesador.cargar_validacion_combinada()
    
    # Visualizar algunas imagenes
    print("\n[PASO 3] Visualizando muestras...")
    if len(X_train) > 0:
        preprocesador.visualizar_imagenes(X_train, y_train, n_muestras=8, 
                                         titulo='Muestras del Dataset Mejorado (Entrenamiento)')
    
    # Guardar arrays preprocesados
    print("\n[PASO 4] Guardando datos preprocesados...")
    os.makedirs('datos_preprocesados', exist_ok=True)
    
    # Guardar datos
    np.save('datos_preprocesados/X_train.npy', X_train)
    np.save('datos_preprocesados/y_train.npy', y_train)
    np.save('datos_preprocesados/X_val.npy', X_val)
    np.save('datos_preprocesados/y_val.npy', y_val)
    
    print("   [OK] Datos guardados en 'datos_preprocesados/':")
    print(f"      - X_train.npy: {X_train.shape}")
    print(f"      - y_train.npy: {y_train.shape}")
    print(f"      - X_val.npy: {X_val.shape}")
    print(f"      - y_val.npy: {y_val.shape}")
    
    # EstadÃ­sticas finales
    print("\n" + "=" * 60)
    print("ESTADISTICAS FINALES")
    print("=" * 60)
    print(f"[INFO] Total de imagenes de entrenamiento: {len(X_train)}")
    print(f"[INFO] Total de imagenes de validacion: {len(X_val)}")
    print(f"[INFO] Ratio entrenamiento/validacion: {len(X_train)/len(X_val) if len(X_val) > 0 else 'N/A':.2f}")
    
    print("\n" + "=" * 60)
    print("[OK] PREPROCESAMIENTO MEJORADO COMPLETADO")
    print("=" * 60)
    print("\n[INFO] Proximo paso: Ejecuta 'python scripts/entrenar_modelo_mejorado.py' para entrenar el modelo")


