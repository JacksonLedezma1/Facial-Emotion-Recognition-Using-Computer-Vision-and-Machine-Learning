# Proyecto de Detección de Emociones Faciales

Este proyecto permite detectar la **emoción principal** en imágenes utilizando la biblioteca [`fer`](https://github.com/justinshenk/fer), combinada con OpenCV y Matplotlib para el procesamiento y visualización de imágenes.

## 📦 Requisitos

Instala las dependencias necesarias con:
```bash
pip install fer opencv-python matplotlib
```
## 🗂️ Dataset de Imágenes

Para que el modelo pueda detectar emociones, es necesario contar con un conjunto de imágenes faciales.

### 🔹 Opción 1: Subir tus propias imágenes

1. Coloca tus imágenes en una carpeta local o en tu Google Drive (si usas Google Colab).
2. Asegúrate de que las imágenes estén en formato compatible como `.jpg`, `.png`, etc.
3. Ejemplo de estructura:


### 🔹 Opción 2: Usar un dataset público

Puedes descargar un dataset de emociones faciales como:

- [FER-2013 (Facial Expression Recognition)](https://www.kaggle.com/datasets/msambare/fer2013)
- [Facial Emotion Recognition Dataset (Extended KUCEV ROMAN)](https://www.kaggle.com/datasets/tapakah68/facial-emotion-recognition?select=images)

Después de descargarlo:

1. Extrae las imágenes.
2. Organiza las carpetas (pueden estar clasificadas por emoción o en una sola carpeta, según tu código).
3. Cambia la ruta en el script Python para apuntar al directorio correcto.

```python
img_dir = "/ruta/a/tu/dataset"
```

##📁 Estructura de Carpetas

Coloca tus imágenes en un directorio. Por ejemplo:
```bash
Proyecto_Final/
└── Quick/
    ├── imagen1.jpg
    ├── imagen2.jpg
    └── ...
```
## 🧠 Código Explicado
```bash
# Importar bibliotecas necesarias
from IPython import get_ipython             # Para trabajar con entornos IPython (como Colab)
from IPython.display import display         # Para mostrar elementos multimedia
from fer import FER                         # Detector de emociones
import cv2                                  # Procesamiento de imágenes
import matplotlib.pyplot as plt             # Visualización
import os                                   # Manejo del sistema de archivos

# Configurar la ruta de las imágenes
img_dir = "/content/drive/MyDrive/Vision_Artificial/Proyecto_Final/Quick"  # Reemplaza con tu ruta

# Obtener la lista de imágenes del directorio
img_files = [f for f in os.listdir(img_dir) if os.path.isfile(os.path.join(img_dir, f))]

# Inicializar el detector de emociones
detector = FER()

# Iterar sobre cada imagen
for img_file in img_files:
    # Cargar imagen
    img_path = os.path.join(img_dir, img_file)
    img = cv2.imread(img_path)

    # Mostrar imagen
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # Convertir de BGR a RGB
    plt.axis('off')
    plt.title(img_file)
    plt.show()

    # Detectar emoción principal
    result = detector.top_emotion(img)
    print(f"{img_file}: {result}")
```
## 📝 Notas

-Este código está pensado para usarse en Google Colab o Jupyter Notebook.

-Asegúrate de montar tu Google Drive si trabajas en Colab.

-La función top_emotion() devuelve una tupla como ('happy', 0.98) representando la emoción detectada y su probabilidad.
