import cv2
import numpy as np

image = cv2.imread("cow.jpg")
print(image.shape)  # (559, 838, 3)

old_width = image.shape[1]  # 838
old_height = image.shape[0]  # 559

# resize by custom size
new_width = 600
new_height = 400
resized = cv2.resize(image, (new_width, new_height))
cv2.imshow("image", resized)

# resize by ratio
width_ratio = 0.5
height_ration = 0.5
resized2 = cv2.resize(image, (0, 0), image, width_ratio, height_ration)
cv2.imshow("image2", resized2)

cv2.waitKey(0)
cv2.destroyAllWindows()
