"""
Script mejorado para entrenar el modelo de clasificación de porciones de comida.

Mejoras:
- Ajustado para datasets más grandes
- Mejor configuración de hiperparámetros
- Más epochs y mejor batch_size
- Callbacks mejorados
"""

import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns

# Configurar para evitar warnings y usar GPU si está disponible
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
physical_devices = tf.config.list_physical_devices('GPU')
if len(physical_devices) > 0:
    print(f"[OK] GPU disponible: {physical_devices[0]}")
    try:
        tf.config.experimental.set_memory_growth(physical_devices[0], True)
    except:
        pass
else:
    print("[INFO] Usando CPU (el entrenamiento sera mas lento)")

class EntrenadorModeloMejorado:
    """
    Clase mejorada para entrenar el modelo de clasificación de porciones.
    """
    
    def __init__(self, img_size=(224, 224), num_classes=2, learning_rate=0.0001):
        """
        Inicializa el entrenador.
        
        Args:
            img_size: Tamaño de las imágenes de entrada
            num_classes: Número de clases (2: correcta, exceso)
            learning_rate: Tasa de aprendizaje inicial
        """
        self.img_size = img_size
        self.num_classes = num_classes
        self.learning_rate = learning_rate
        self.model = None
        self.history = None
    
    def construir_modelo(self):
        """
        Construye el modelo usando Transfer Learning con MobileNetV2.
        """
        print("\n[INFO] Construyendo modelo...")
        
        # Base model: MobileNetV2 pre-entrenado
        base_model = MobileNetV2(
            input_shape=(*self.img_size, 3),
            include_top=False,
            weights='imagenet'
        )
        
        # Congelar las primeras capas (transfer learning)
        base_model.trainable = True
        # Descongelar las últimas capas para fine-tuning
        fine_tune_at = len(base_model.layers) - 30
        for layer in base_model.layers[:fine_tune_at]:
            layer.trainable = False
        
        # Construir modelo completo
        inputs = keras.Input(shape=(*self.img_size, 3))
        
        # Preprocesamiento MobileNetV2
        x = tf.keras.applications.mobilenet_v2.preprocess_input(inputs)
        
        # Base model
        x = base_model(x, training=False)
        
        # Global Average Pooling
        x = layers.GlobalAveragePooling2D()(x)
        
        # Dropout para regularización
        x = layers.Dropout(0.3)(x)
        
        # Capa densa adicional
        x = layers.Dense(128, activation='relu')(x)
        x = layers.Dropout(0.3)(x)
        
        # Capa de salida
        outputs = layers.Dense(self.num_classes, activation='softmax')(x)
        
        self.model = keras.Model(inputs, outputs)
        
        # Compilar modelo
        self.model.compile(
            optimizer=keras.optimizers.Adam(learning_rate=self.learning_rate),
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']
        )
        
        print("[OK] Modelo construido")
        print(f"   Total de parámetros: {self.model.count_params():,}")
    
    def crear_data_augmentation(self):
        """
        Crea el generador de data augmentation.
        """
        return ImageDataGenerator(
            rotation_range=20,
            width_shift_range=0.2,
            height_shift_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True,
            fill_mode='nearest'
        )
    
    def entrenar(self, X_train, y_train, X_val, y_val, epochs=100, batch_size=16):
        """
        Entrena el modelo.
        
        Args:
            X_train: Imágenes de entrenamiento
            y_train: Etiquetas de entrenamiento
            X_val: Imágenes de validación
            y_val: Etiquetas de validación
            epochs: Número de épocas
            batch_size: Tamaño del batch
        """
        print("\n" + "=" * 60)
        print("[INICIO] INICIANDO ENTRENAMIENTO MEJORADO")
        print("=" * 60)
        
        if self.model is None:
            self.construir_modelo()
        
        # Crear directorio para modelos
        os.makedirs('modelos', exist_ok=True)
        os.makedirs('documentacion', exist_ok=True)
        
        # Callbacks mejorados
        callbacks = [
            EarlyStopping(
                monitor='val_loss',
                patience=15,  # Más paciencia para datasets más grandes
                restore_best_weights=True,
                verbose=1,
                mode='min'
            ),
            ReduceLROnPlateau(
                monitor='val_loss',
                factor=0.5,
                patience=7,
                min_lr=1e-7,
                verbose=1,
                mode='min'
            ),
            ModelCheckpoint(
                'modelos/mejor_modelo.h5',
                monitor='val_accuracy',
                save_best_only=True,
                verbose=1,
                mode='max'
            )
        ]
        
        # Preprocesar imágenes para MobileNetV2
        print("\n[INFO] Preprocesando imagenes...")
        X_train_prep = tf.keras.applications.mobilenet_v2.preprocess_input(X_train * 255.0)
        X_val_prep = tf.keras.applications.mobilenet_v2.preprocess_input(X_val * 255.0)
        
        print(f"[OK] Datos preprocesados")
        print(f"   Training: {X_train_prep.shape}")
        print(f"   Validation: {X_val_prep.shape}")
        
        # Entrenar modelo
        print(f"\n[INFO] Entrenando con {len(X_train)} imagenes de entrenamiento...")
        print(f"   Validando con {len(X_val)} imágenes...")
        print(f"   Batch size: {batch_size}")
        print(f"   Epochs máximos: {epochs}")
        print("\n[INFO] Iniciando entrenamiento (esto puede tardar varios minutos)...\n")
        
        # Entrenar
        self.history = self.model.fit(
            X_train_prep, y_train,
            validation_data=(X_val_prep, y_val),
            epochs=epochs,
            batch_size=batch_size,
            callbacks=callbacks,
            verbose=1
        )
        
        print("\n[OK] Entrenamiento completado")
    
    def evaluar(self, X_val, y_val):
        """
        Evalúa el modelo en el conjunto de validación.
        """
        print("\n" + "=" * 60)
        print("[INFO] EVALUANDO MODELO")
        print("=" * 60)
        
        X_val_prep = tf.keras.applications.mobilenet_v2.preprocess_input(X_val * 255.0)
        
        # Evaluar
        loss, accuracy = self.model.evaluate(X_val_prep, y_val, verbose=0)
        
        print(f"\n[OK] Precision en validacion: {accuracy * 100:.2f}%")
        print(f"[OK] Perdida en validacion: {loss:.4f}")
        
        # Predicciones para matriz de confusión
        y_pred_proba = self.model.predict(X_val_prep, verbose=0)
        y_pred = np.argmax(y_pred_proba, axis=1)
        
        # Reporte de clasificación
        print("\n📋 Reporte de Clasificación:")
        print(classification_report(y_val, y_pred, 
                                   target_names=['Porcion Correcta', 'Exceso Porcion']))
        
        # Matriz de confusión
        cm = confusion_matrix(y_val, y_pred)
        
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                   xticklabels=['Porcion Correcta', 'Exceso Porcion'],
                   yticklabels=['Porcion Correcta', 'Exceso Porcion'])
        plt.title('Matriz de Confusión')
        plt.ylabel('Etiqueta Real')
        plt.xlabel('Etiqueta Predicha')
        plt.tight_layout()
        plt.savefig('documentacion/matriz_confusion_mejorada.png', dpi=150, bbox_inches='tight')
        print("\n[OK] Matriz de confusion guardada en: documentacion/matriz_confusion_mejorada.png")
        plt.close()
    
    def graficar_historial(self):
        """
        Grafica el historial de entrenamiento.
        """
        if self.history is None:
            print("[ADVERTENCIA] No hay historial de entrenamiento para graficar")
            return
        
        fig, axes = plt.subplots(1, 2, figsize=(15, 5))
        
        # Accuracy
        axes[0].plot(self.history.history['accuracy'], label='Training Accuracy')
        axes[0].plot(self.history.history['val_accuracy'], label='Validation Accuracy')
        axes[0].set_title('Precisión del Modelo')
        axes[0].set_xlabel('Época')
        axes[0].set_ylabel('Precisión')
        axes[0].legend()
        axes[0].grid(True)
        
        # Loss
        axes[1].plot(self.history.history['loss'], label='Training Loss')
        axes[1].plot(self.history.history['val_loss'], label='Validation Loss')
        axes[1].set_title('Pérdida del Modelo')
        axes[1].set_xlabel('Época')
        axes[1].set_ylabel('Pérdida')
        axes[1].legend()
        axes[1].grid(True)
        
        plt.tight_layout()
        plt.savefig('documentacion/historial_entrenamiento_mejorado.png', dpi=150, bbox_inches='tight')
        print("[OK] Historial guardado en: documentacion/historial_entrenamiento_mejorado.png")
        plt.close()
    
    def guardar_modelo(self, ruta='modelos/modelo_porciones.keras'):
        """
        Guarda el modelo entrenado.
        """
        if self.model is None:
            print("[ADVERTENCIA] No hay modelo para guardar")
            return
        
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        self.model.save(ruta)
        print(f"\n[OK] Modelo guardado en: {ruta}")


if __name__ == "__main__":
    print("=" * 60)
    print("[INICIO] ENTRENAMIENTO MEJORADO DEL MODELO")
    print("Clasificación de Porciones de Comida")
    print("=" * 60)
    
    # 1. Cargar datos preprocesados
    print("\n[PASO 1] Cargando datos preprocesados...")
    try:
        X_train = np.load('datos_preprocesados/X_train.npy')
        y_train = np.load('datos_preprocesados/y_train.npy')
        X_val = np.load('datos_preprocesados/X_val.npy')
        y_val = np.load('datos_preprocesados/y_val.npy')
        print("   [OK] Datos cargados correctamente")
        print(f"   [INFO] Training: {X_train.shape}, Validation: {X_val.shape}")
    except FileNotFoundError:
        print("   ❌ No se encontraron datos preprocesados.")
        print("   [INFO] Ejecuta primero: python scripts/preprocesamiento.py")
        exit(1)
    
    # 2. Calcular batch_size óptimo
    dataset_size = len(X_train)
    if dataset_size < 50:
        batch_size = 8
    elif dataset_size < 100:
        batch_size = 16
    else:
        batch_size = 32
    
    print(f"\n   [INFO] Batch size calculado: {batch_size} (basado en dataset de {dataset_size} imagenes)")
    
    # 3. Crear y entrenar modelo
    print("\n[PASO 2] Creando entrenador mejorado...")
    entrenador = EntrenadorModeloMejorado(img_size=(224, 224), num_classes=2, learning_rate=0.0001)
    
    print("\n[PASO 3] Construyendo modelo...")
    entrenador.construir_modelo()
    
    # Mostrar resumen
    print("\n[INFO] Resumen del modelo:")
    entrenador.model.summary()
    
    # 4. Entrenar
    print("\n[PASO 4] Iniciando entrenamiento...")
    entrenador.entrenar(
        X_train, y_train,
        X_val, y_val,
        epochs=100,  # Más epochs para mejor convergencia
        batch_size=batch_size
    )
    
    # 5. Evaluar modelo
    print("\n[PASO 5] Evaluando modelo...")
    entrenador.evaluar(X_val, y_val)
    
    # 6. Graficar historial
    print("\n[PASO 6] Generando graficos...")
    entrenador.graficar_historial()
    
    # 7. Guardar modelo final
    print("\n[PASO 7] Guardando modelo...")
    entrenador.guardar_modelo('modelos/modelo_porciones.keras')
    
    print("\n" + "=" * 60)
    print("[OK] ENTRENAMIENTO MEJORADO COMPLETADO")
    print("=" * 60)
    print("\n[INFO] El modelo mejorado esta listo para usar en produccion")

