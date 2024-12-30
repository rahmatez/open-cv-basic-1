import cv2
import numpy as np

# Membaca gambar dengan OpenCV
image = cv2.imread('assets/gambar1.jpg')

# Menentukan jumlah pergeseran horizontal dan vertikal
tx = 50  # Pergeseran horizontal
ty = 30  # Pergeseran vertikal

# Membuat matriks translasi
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])

# Melakukan translasi pada gambar
translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))

# Menampilkan gambar asli dan hasil translasi
cv2.imshow('Original Image', image)
cv2.imshow('Translated Image', translated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
