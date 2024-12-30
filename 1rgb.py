import cv2

# Membaca gambar dengan OpenCV
image = cv2.imread('assets/gambar1.jpg')

# Mengubah gambar ke format RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Menampilkan gambar asli dan gambar RGB
cv2.imshow('Original Image (21102043)', image)
cv2.imshow('RGB Image (21102043)', image_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()