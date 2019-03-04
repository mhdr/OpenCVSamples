import cv2
import numpy as np

blank_image = np.zeros([512, 512, 3], dtype=np.uint8)


def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(blank_image, center=(x, y), radius=20, color=(0, 0, 255), thickness=-1)


cv2.namedWindow("image")
cv2.setMouseCallback("image", draw_circle)

while True:
    cv2.imshow("image", blank_image)

    # wait 5 seconds then wait for ESC key
    if cv2.waitKey(5) & 0xFF == 27:
        break

cv2.destroyAllWindows()
