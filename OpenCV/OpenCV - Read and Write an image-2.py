
#Read an image, then show the image in a window and destroy on amy key stroke
import cv2

# Load an color image in grayscale
img = cv2.imread('OpenCV\mypython.png',1)

#cv2.IMREAD_COLOR : Loads a color image; use 1
#cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode ; use 0

cv2.imshow('my image',img)
cv2.waitKey(0)

img1 = cv2.imwrite('newpython.jpg',img)

img2 = cv2.imread('newpython.jpg',0)
cv2.imshow('New image',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
