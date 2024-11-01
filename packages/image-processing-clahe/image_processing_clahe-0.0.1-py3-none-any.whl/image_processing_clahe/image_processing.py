import cv2
import matplotlib.pyplot as plt

def load_image(image_path):
    # Carrega uma imagem a partir do caminho especificado.
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Não foi possível carregar a imagem do caminho: {image_path}")
    return img

def apply_clahe(img):
    # Aplica o CLAHE a uma imagem.
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    clahe_l = clahe.apply(l)
    lab_clahe = cv2.merge((clahe_l, a, b))
    return cv2.cvtColor(lab_clahe, cv2.COLOR_LAB2BGR)

def display_images(original_img, processed_img):
    # Visualiza a imagem original e a processada.
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB))
    plt.title('Imagem Original')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB))
    plt.title('Imagem com CLAHE')
    plt.show()
