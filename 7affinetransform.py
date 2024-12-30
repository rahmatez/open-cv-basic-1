import cv2
import numpy as np

# Membaca gambar dengan OpenCV
image = cv2.imread('assets/gambar1.jpg')

# Mendefinisikan titik-titik pada gambar asli
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])

# Mendefinisikan titik-titik pada gambar hasil transformasi
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

# Membuat matriks transformasi affine
matrix = cv2.getAffineTransform(pts1, pts2)

# Melakukan transformasi affine pada gambar
affine_transformed_image = cv2.warpAffine(image, matrix, (image.shape[1], image.shape[0]))

# Menampilkan gambar asli dan hasil transformasi affine
cv2.imshow('Original Image', image)
cv2.imshow('Affine Transformed Image', affine_transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
