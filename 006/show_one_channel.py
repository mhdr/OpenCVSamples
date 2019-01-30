import cv2
import numpy as np

image: np.ndarray = cv2.imread("cow.jpg")
# channels : BGR => 0,1,2
image2 = image[:, :, 1]
cv2.imshow("image", image2)

cv2.waitKey(0)
cv2.destroyAllWindows()
