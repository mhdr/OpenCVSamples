import cv2
import numpy as np

image:np.ndarray = cv2.imread("cow.jpg")
print(image.shape)