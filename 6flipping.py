import cv2

# Membaca gambar dengan OpenCV
image = cv2.imread('assets/gambar1.jpg')

# Melakukan flipping horizontal
flipped_horizontal = cv2.flip(image, 1)

# Melakukan flipping vertikal
flipped_vertical = cv2.flip(image, 0)

# Melakukan flipping horizontal dan vertikal
flipped_both = cv2.flip(image, -1)

# Menampilkan gambar asli dan hasil flipping
cv2.imshow('Original Image', image)
cv2.imshow('Flipped Horizontal', flipped_horizontal)
cv2.imshow('Flipped Vertical', flipped_vertical)
cv2.imshow('Flipped Both', flipped_both)
cv2.waitKey(0)
cv2.destroyAllWindows()
