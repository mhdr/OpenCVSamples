import cv2
import numpy as np
import pprint

image = cv2.imread('cow.jpg', cv2.IMREAD_COLOR)
print(image.shape)
print(image.size)
print(image.dtype)
