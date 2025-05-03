
# 1. DETECCIÓN DEL ROSTRO
# -----------------------
# El modelo utiliza un detector de rostros (por ejemplo, MTCNN, Haar cascades o CNN)
# para localizar la región facial en una imagen de entrada.
#
# Matemáticamente:
#    Región_rostro = D(I)
# Donde:
#    - I: imagen original
#    - D: función de detección de rostro (modelo)
#    - Región_rostro: coordenadas del rostro detectado

# 2. PREPROCESAMIENTO DEL ROSTRO
# ------------------------------
# La región facial detectada se transforma a escala de grises y se redimensiona,
# normalmente a 48x48 píxeles.
#
# Fórmula:
#    I' = resize(gray(Región_rostro))
# Esto estandariza la entrada para el modelo CNN.

# 3. EXTRACCIÓN DE CARACTERÍSTICAS (CNN)
# --------------------------------------
# Se utilizan redes neuronales convolucionales (CNN) para extraer patrones visuales del rostro.
# Cada capa convolucional realiza:
#
#    F_i = f(W_i * I' + b_i)
#
# Donde:
#    - W_i: filtros (kernels) aprendidos en la capa i
#    - * : operación de convolución
#    - b_i: sesgo (bias)
#    - f : función de activación, como ReLU
#    - F_i: mapa de características extraído

# 4. CLASIFICACIÓN DE EMOCIONES
# -----------------------------
# Al final, se aplica una capa densa (fully connected) seguida de una softmax,
# que produce un vector de probabilidades para cada emoción:
#
#    p = softmax(z)
#    softmax(z_i) = e^(z_i) / Σ_j e^(z_j)
#
# Donde:
#    - z: vector de puntuaciones no normalizadas
#    - p: vector de probabilidades para cada emoción

# 5. RESULTADO FINAL
# ------------------
# Se selecciona la emoción con la probabilidad más alta:
#    resultado = max(p)
#
# Ejemplo:
#    ('happy', 0.94)  -> el modelo predice "feliz" con 94% de confianza

