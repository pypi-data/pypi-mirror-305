# pip install opencv-python
# pip install matplotlib

import cv2
import matplotlib.pyplot as plt

# Carrega a imagem
def process_image(image_path):
    img = cv2.imread(image_path)
    
    # Verifica se a imagem foi carregada corretamente
    if img is None:
        raise ValueError(f"Não foi possível carregar a imagem do caminho: {image_path}")
    
    # Separa os canais de cor
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    # Cria o objeto CLAHE
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    clahe_l = clahe.apply(l)

    # Recombina os canais
    lab_clahe = cv2.merge((clahe_l, a, b))
    final_img = cv2.cvtColor(lab_clahe, cv2.COLOR_LAB2BGR)

    # Visualiza as imagens
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Imagem Original')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(final_img, cv2.COLOR_BGR2RGB))
    plt.title('Imagem com CLAHE')
    plt.show()
