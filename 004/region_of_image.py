import cv2
import numpy as np
import pprint

image = cv2.imread('cow.jpg', cv2.IMREAD_COLOR)
image[150:200, 100:150] = [255, 255, 255]
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
