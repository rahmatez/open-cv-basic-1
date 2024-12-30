import cv2

# Membaca gambar dengan OpenCV
image = cv2.imread('assets/gambar1.jpg')

# Menentukan koordinat batas pemotongan (crop)
x = 100  # Koordinat x (titik awal horizontal)
y = 100   # Koordinat y (titik awal vertikal)
w = 200 # Lebar pemotongan
h = 200  # Tinggi pemotongan

# Melakukan pemotongan (crop) pada gambar
cropped_image = image[y:y+h, x:x+w]

# Menampilkan gambar asli dan hasil cropping
cv2.imshow('Original Image', image)
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()