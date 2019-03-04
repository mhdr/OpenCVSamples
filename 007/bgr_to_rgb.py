import cv2
import numpy as np

image = cv2.imread("cow.jpg")
cv2.imshow("image", image)

fixed = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow("image2", fixed)

image_gray = cv2.imread("cow.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("image3", image_gray)

image_gray2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("image4", image_gray2)

cv2.waitKey(0)
cv2.destroyAllWindows()
