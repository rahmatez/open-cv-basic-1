# import required libraries
import cv2
import numpy as np

# read the input color image
img = cv2.imread('assets/gambar1.jpg')

# split the Blue, Green and Red color channels
blue,green,red = cv2.split(img)

# define channel having all zeros
zeros = np.zeros(blue.shape, np.uint8)

# merge zeros to make BGR image
blueBGR = cv2.merge([blue,zeros,zeros])
greenBGR = cv2.merge([zeros,green,zeros])
redBGR = cv2.merge([zeros,zeros,red])

# display the three Blue, Green, and Red channels as BGR image
cv2.imshow('Blue Channel', blueBGR)
cv2.imshow('Green Channel', greenBGR)
cv2.imshow('Red Channel', redBGR)
cv2.waitKey(0)
cv2.destroyAllWindows()