import cv2
import numpy as np

image1 = cv2.imread("cow.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow("Image 1",image1)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("cow2.jpg",image1)