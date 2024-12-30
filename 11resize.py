import cv2

# Membaca gambar dengan OpenCV
image = cv2.imread('assets/gambar1.jpg')

# Mengubah ukuran gambar menjadi 30x30
resized_30x30 = cv2.resize(image, (30, 30))

# Mengubah ukuran gambar menjadi 90x90
resized_90x90 = cv2.resize(image, (90, 90))

# Mengubah ukuran gambar menjadi 120x120
resized_120x120 = cv2.resize(image, (120, 120))

# Menampilkan gambar yang sudah diresize
cv2.imshow('Resized 30x30', resized_30x30)
cv2.imshow('Resized 90x90', resized_90x90)
cv2.imshow('Resized 120x120', resized_120x120)
cv2.waitKey(0)
cv2.destroyAllWindows()
