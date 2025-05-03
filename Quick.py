from IPython import get_ipython
from IPython.display import display
from fer import FER
import cv2
import matplotlib.pyplot as plt
import os

# Directorio donde se encuentran las imágenes
img_dir = "/content/drive/MyDrive/Vision_Artificial/Proyecto_Final/Quick"  # Reemplaza con la ruta de tu directorio

# Obtener una lista de todos los archivos en el directorio
img_files = [f for f in os.listdir(img_dir) if os.path.isfile(os.path.join(img_dir, f))]

# Iterar sobre cada archivo de imagen
for img_file in img_files:
    # Ruta completa de la imagen
    img_path = os.path.join(img_dir, img_file)

    # Cargar la imagen
    img = cv2.imread(img_path)

    # Verificar si la imagen se cargó correctamente
    if img is None:
        print(f"Error: No se pudo cargar la imagen desde {img_path}. Verifica la ruta del archivo y asegúrate de que la imagen exista.")
        continue  # Saltar a la siguiente imagen si hay un error

    # Mostrar la imagen usando matplotlib
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # Convertir de BGR a RGB para matplotlib
    plt.axis('off')  # Ocultar los ejes
    plt.title(img_file) # Mostrar el nombre del archivo como título
    plt.show()

    # Detectar la emoción
    detector = FER()
    result = detector.top_emotion(img)
    print(result)
