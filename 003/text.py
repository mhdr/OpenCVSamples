import cv2
import numpy as np

image = cv2.imread("cow.jpg")

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, "OpenCV Tutorial", (0, 130), font, 2, (0, 0, 255), 3, cv2.LINE_AA)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
