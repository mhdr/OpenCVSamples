import cv2
import numpy as np

image = cv2.imread("cow.jpg")

cv2.line(image,(0,0),(100,100),(255,255,0),20)

cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()