# 🚀 Guía de Entrenamiento Mejorado

Esta guía explica cómo usar los scripts mejorados que combinan el dataset original con el nuevo dataset expandido de `Pruebas-ensambladas/`.

## 📊 Mejoras del Dataset

### Dataset Original
- **Porcion_correcta**: 11 imágenes
- **Exceso_porcion**: 9 imágenes
- **Total entrenamiento**: 20 imágenes

### Nuevo Dataset (Pruebas-ensambladas)
- **Porcion_correcta**: ~77 imágenes
- **Exceso_porcion**: ~63 imágenes
- **Total entrenamiento**: ~140 imágenes

### Dataset Combinado
- **Total entrenamiento**: ~160 imágenes (8x más que el original)
- **Mejor balance**: Más ejemplos para entrenar un modelo más robusto
- **Mayor diversidad**: Más variaciones de imágenes de comida

## 🔄 Flujo de Trabajo

### Paso 1: Preprocesamiento Mejorado

```bash
# Activa el entorno virtual
.venv\Scripts\Activate.ps1

# Ejecuta el preprocesamiento mejorado
python scripts/preprocesamiento_mejorado.py
```

**Qué hace:**
- ✅ Combina imágenes de `entrenamiento/` y `Pruebas-ensambladas/Entrnamiento_*`
- ✅ Combina imágenes de `validacion/` y `Pruebas-ensambladas/Validacion_*`
- ✅ Redimensiona todas las imágenes a 224x224
- ✅ Normaliza los valores de píxeles
- ✅ Guarda los datos preprocesados en `datos_preprocesados/`
- ✅ Genera visualización de muestras

**Output esperado:**
```
✅ Total de imágenes cargadas: ~160
📊 Forma de X: (160, 224, 224, 3)
   - Porcion_correcta: ~88 imágenes
   - Exceso_porcion: ~72 imágenes
```

### Paso 2: Entrenamiento Mejorado

```bash
# Ejecuta el entrenamiento mejorado
python scripts/entrenar_modelo_mejorado.py
```

**Mejoras del entrenamiento:**
- ✅ Batch size automático según tamaño del dataset
- ✅ Más epochs (100 vs 50) para mejor convergencia
- ✅ Mejor configuración de callbacks (EarlyStopping, ReduceLR, etc.)
- ✅ Fine-tuning mejorado del modelo base
- ✅ Regularización con Dropout

**Tiempo estimado:**
- CPU: 30-60 minutos
- GPU: 5-15 minutos

### Paso 3: Verificar Resultados

Después del entrenamiento, revisa:
- `documentacion/historial_entrenamiento_mejorado.png` - Gráficos de entrenamiento
- `documentacion/matriz_confusion_mejorada.png` - Matriz de confusión
- `modelos/modelo_porciones.keras` - Modelo entrenado

## 📁 Estructura de Carpetas

```
IBM_Inteligente/
├── entrenamiento/              # Dataset original
│   ├── Porcion_correcta/       # 11 imágenes
│   └── Exceso_porcion/         # 9 imágenes
│
├── Pruebas-ensambladas/        # Nuevo dataset
│   ├── Entrnamiento_Porcioncorrecta/    # ~77 imágenes
│   ├── Entrenamiento_Excesoporcion/     # ~63 imágenes
│   ├── Validacion_Porcioncorrecta/      # ~35 imágenes
│   └── Validacion_Excesoporcion/        # ~28 imágenes
│
├── validacion/                 # Dataset original de validación
│   ├── Porcioncorrecta/
│   └── Porcionexceso/
│
├── scripts/
│   ├── preprocesamiento_mejorado.py    # ⭐ Nuevo script
│   ├── entrenar_modelo_mejorado.py     # ⭐ Nuevo script
│   └── predecir.py                     # Usa el modelo mejorado
│
└── datos_preprocesados/        # Se crea automáticamente
    ├── X_train.npy
    ├── y_train.npy
    ├── X_val.npy
    └── y_val.npy
```

## 🎯 Resultados Esperados

Con el dataset mejorado, deberías ver:

### Métricas Mejoradas:
- **Accuracy**: >85% (vs ~70-80% con dataset pequeño)
- **Precisión**: Mejor balance entre clases
- **Recall**: Menos falsos negativos
- **F1-Score**: >0.85

### Ventajas:
1. ✅ Modelo más robusto y generalizable
2. ✅ Menos overfitting (más datos = mejor generalización)
3. ✅ Mejor rendimiento en casos edge
4. ✅ Predicciones más confiables

## 🔧 Configuración Avanzada

### Ajustar Hiperparámetros

En `entrenar_modelo_mejorado.py` puedes modificar:

```python
# Tasa de aprendizaje
learning_rate=0.0001  # Más bajo para fine-tuning

# Batch size (se calcula automáticamente, pero puedes forzarlo)
batch_size=32  # Para datasets grandes

# Epochs
epochs=100  # Más epochs para mejor convergencia

# Data augmentation
rotation_range=20      # Rotación de imágenes
zoom_range=0.2         # Zoom aleatorio
horizontal_flip=True   # Volteo horizontal
```

### Usar GPU

Si tienes GPU disponible, TensorFlow la detectará automáticamente. Para verificar:

```python
import tensorflow as tf
print(tf.config.list_physical_devices('GPU'))
```

## ⚠️ Solución de Problemas

### Error: "No se encontraron datos preprocesados"

**Solución:** Ejecuta primero `preprocesamiento_mejorado.py`

### Error: "CUDA out of memory"

**Solución:** Reduce el batch_size en `entrenar_modelo_mejorado.py`:
```python
batch_size=16  # o 8 si sigue sin funcionar
```

### Error: Carpeta no encontrada

El script maneja automáticamente carpetas faltantes. Si ves advertencias, verifica que las carpetas existan:
- `Pruebas-ensambladas/Entrnamiento_Porcioncorrecta`
- `Pruebas-ensambladas/Entrenamiento_Excesoporcion`

### El entrenamiento es muy lento

- Usa GPU si está disponible
- Reduce el batch_size
- Reduce el número de epochs (aunque esto puede afectar la calidad)

## 📈 Comparación de Resultados

### Dataset Original (20 imágenes)
- Accuracy: ~70-80%
- Overfitting: Alto
- Generalización: Baja

### Dataset Mejorado (160 imágenes)
- Accuracy: >85%
- Overfitting: Bajo
- Generalización: Alta
- Confianza: Mayor en predicciones

## 🚀 Próximos Pasos

Después de entrenar el modelo mejorado:

1. **Probar el modelo:**
   ```bash
   python scripts/predecir.py validacion/Porcioncorrecta/v1.jpg
   ```

2. **Reemplazar el modelo en producción:**
   - El modelo se guarda en `modelos/modelo_porciones.keras`
   - El backend lo carga automáticamente si tiene el mismo nombre

3. **Evaluar en nuevas imágenes:**
   - Usa la aplicación web para probar con tus propias imágenes
   - Compara resultados con el modelo anterior

## 💡 Tips

- **Mantén backups:** Guarda el modelo anterior antes de reemplazarlo
- **Entrena en horarios de bajo uso:** El entrenamiento puede ser intensivo
- **Monitorea el entrenamiento:** Revisa los gráficos para detectar overfitting
- **Itera:** Si los resultados no son buenos, ajusta hiperparámetros y vuelve a entrenar

---

**¡Listo! Ahora tienes un modelo mejor entrenado con mucho más datos.** 🎉

