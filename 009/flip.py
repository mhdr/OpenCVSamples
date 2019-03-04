import cv2
import numpy as np

image = cv2.imread("cow.jpg")
cv2.imshow("image", image)

# flip horizontally
flipped1 = cv2.flip(image, 0)
cv2.imshow("image1", flipped1)

# flip vertically
flipped2 = cv2.flip(image, 1)
cv2.imshow("image2", flipped2)

# flip both horizontally and vertically
flipped3 = cv2.flip(image, -1)
cv2.imshow("image3", flipped3)

cv2.waitKey(0)
cv2.destroyAllWindows()
