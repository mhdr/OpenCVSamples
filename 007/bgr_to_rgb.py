import cv2
import numpy as np

image = cv2.imread("cow.jpg")
cv2.imshow("image", image)

fixed = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow("image2", fixed)

cv2.waitKey(0)
cv2.destroyAllWindows()
