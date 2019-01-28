import cv2
import numpy as np
import pprint

image = cv2.imread('cow.jpg',cv2.IMREAD_COLOR)
pixel= image[55,55]
pprint.pprint(pixel)