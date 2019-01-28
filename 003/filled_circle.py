import cv2
import numpy as np

image = cv2.imread("cow.jpg")

cv2.circle(image,(100,100),40,(255,255,0),-1)

cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()