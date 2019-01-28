import cv2
import numpy as np
import pprint

image = cv2.imread('cow.jpg', cv2.IMREAD_COLOR)
image[55, 55] = [255, 255, 255]
pixel = image[55, 55]
pprint.pprint(pixel)
