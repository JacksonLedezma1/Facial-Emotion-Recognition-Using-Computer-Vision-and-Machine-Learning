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
# Filter for image files only - this is the key fix
img_files = [
    f
    for f in os.listdir(img_dir)
    if os.path.isfile(os.path.join(img_dir, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg'))
]

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
    result = detector.top_emotion(img) # Se detecta la emoción principal en la imagen.
    print(f"{img_file}: {result}")
