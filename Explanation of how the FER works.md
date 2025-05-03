"""
📘 Explicación matemática del modelo FER (Facial Expression Recognition)
Autor: [Tu Nombre o Usuario de GitHub]

Este módulo describe, con anotaciones y fórmulas, cómo funciona un modelo de reconocimiento
de expresiones faciales usando redes neuronales convolucionales (CNN), como el que usa la biblioteca `fer`.

--------------------------------------------
🔹 1. Detección del rostro
--------------------------------------------

El sistema detecta automáticamente la región del rostro en una imagen.

📐 Fórmula:
    Región_rostro = D(I)

🔸 Donde:
    - I: Imagen original
    - D: Modelo de detección (por ejemplo, Haar cascades, MTCNN, CNN)
    - Región_rostro: Coordenadas de la región facial detectada

--------------------------------------------
🔹 2. Preprocesamiento
--------------------------------------------

Una vez detectado, el rostro se convierte a escala de grises y se redimensiona.

📐 Fórmula:
    I' = resize(gray(Región_rostro))

🔸 Estándar común: 48x48 píxeles, en escala de grises

--------------------------------------------
🔹 3. Extracción de características (CNN)
--------------------------------------------

Las redes convolucionales extraen patrones visuales a través de filtros.

📐 Fórmula:
    Fᵢ = f(Wᵢ * I' + bᵢ)

🔸 Donde:
    - Wᵢ: Filtros (kernels) de la capa i
    - * : Convolución
    - bᵢ: Sesgo (bias)
    - f : Función de activación (e.g., ReLU)
    - Fᵢ: Mapa de características generado

--------------------------------------------
🔹 4. Clasificación de emociones
--------------------------------------------

Las características se pasan por capas densas y una capa softmax.

📐 Fórmula:
    p = softmax(z)

    softmax(zᵢ) = e^(zᵢ) / Σⱼ e^(zⱼ)

🔸 Donde:
    - z: Vector de salida de la red antes de la activación
    - p: Vector de probabilidades de cada emoción

--------------------------------------------
🔹 5. Resultado final
--------------------------------------------

La emoción más probable es la salida del modelo.

📦 Ejemplo de salida:
    ('happy', 0.94)

→ Indica que la emoción predicha es “feliz” con 94% de confianza.
"""

# Este archivo es de uso educativo. Puede ser combinado con un script de inferencia con FER.
