import cv2
import numpy as np
import pprint

image = cv2.imread("cow.jpg")

points = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
points = points.reshape(-1, 1, 2)
cv2.polylines(image, [points], True, (255, 255, 0), 3)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
