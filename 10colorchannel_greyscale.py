import cv2

# Membaca gambar dengan OpenCV
image = cv2.imread('assets/gambar1.jpg')

# Memisahkan saluran warna
blue_channel, green_channel, red_channel = cv2.split(image)

# Menampilkan saluran warna secara terpisah
cv2.imshow('Blue Channel', blue_channel)
cv2.imshow('Green Channel', green_channel)
cv2.imshow('Red Channel', red_channel)
cv2.waitKey(0)
cv2.destroyAllWindows()
