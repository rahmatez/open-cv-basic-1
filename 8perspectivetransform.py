import cv2
import numpy as np

# Membaca gambar dengan OpenCV
image = cv2.imread('assets/gambar1.jpg')

# Mendefinisikan titik-titik pada gambar asli
pts1 = np.float32([[50, 50], [200, 50], [50, 200], [200, 200]])

# Mendefinisikan titik-titik pada gambar hasil transformasi
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

# Membuat matriks transformasi perspektif
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Melakukan transformasi perspektif pada gambar
perspective_transformed_image = cv2.warpPerspective(image, matrix, (300, 300))

# Menampilkan gambar asli dan hasil transformasi perspektif
cv2.imshow('Original Image', image)
cv2.imshow('Perspective Transformed Image', perspective_transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
