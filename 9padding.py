import cv2
import numpy as np

# Membaca gambar dengan OpenCV
image = cv2.imread('assets/gambar1.jpg')

# Menentukan jumlah padding untuk setiap sisi (top, bottom, left, right)
top = 20
bottom = 20
left = 30
right = 30

# Membuat warna padding (dalam skala BGR)
padding_color = [0, 0, 0]  # Hitam

# Menambahkan padding ke gambar
padded_image = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=padding_color)

# Menampilkan gambar asli dan gambar dengan padding
cv2.imshow('Original Image', image)
cv2.imshow('Padded Image', padded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
