import cv2
import numpy as np
import pprint

image = cv2.imread('cow.jpg', cv2.IMREAD_COLOR)

watch_face = image[200:250,107:194]
image[0:50,0:87] = watch_face

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()