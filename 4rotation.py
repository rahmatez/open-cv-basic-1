import cv2

# Membaca gambar dengan OpenCV
image = cv2.imread('assets/gambar1.jpg')

# Menentukan sudut rotasi (dalam derajat)
angle = 180

# Menghitung setengah lebar dan tinggi gambar
height, width = image.shape[:2]
half_height = height // 2
half_width = width // 2

# Mendefinisikan matriks rotasi
rotation_matrix = cv2.getRotationMatrix2D((half_width, half_height), angle, 1)

# Melakukan rotasi pada gambar
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

# Menampilkan gambar asli dan hasil rotasi
cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
