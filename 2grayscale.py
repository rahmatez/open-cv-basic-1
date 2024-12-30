import cv2

# Membaca gambar dengan OpenCV
image = cv2.imread('assets/gambar1.jpg')

# Mengubah gambar ke citra grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Menampilkan gambar asli dan citra grayscale
cv2.imshow('Original Image (21102043)', image)
cv2.imshow('Grayscale Image (21102043)', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
