import cv2
import numpy as np

image: np.ndarray = cv2.imread("cow.jpg")
image2 = image.copy()
# channels : BGR => 0,1,2
image2[:, :, 0] = 0
image2[:, :, 1] = 0
cv2.imshow("image", image2)

cv2.waitKey(0)
cv2.destroyAllWindows()
