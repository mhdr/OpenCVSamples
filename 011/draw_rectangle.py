import cv2
import numpy as np

is_drawing = False
ix = -1
iy = -1

blank_image = np.zeros([512, 512, 3], dtype=np.uint8)


def draw_rectangle(event, x, y, flags, param):
    global is_drawing, ix, iy

    if event == cv2.EVENT_LBUTTONDOWN:
        is_drawing = True
        ix = x
        iy = y
    elif event == cv2.EVENT_LBUTTONUP:
        is_drawing = False
        cv2.rectangle(img=blank_image, pt1=(ix, iy), pt2=(x, y), color=(255, 0, 0), thickness=-1)
        ix = -1
        iy = -1
    elif event == cv2.EVENT_MOUSEMOVE:
        if is_drawing:
            cv2.rectangle(img=blank_image, pt1=(ix, iy), pt2=(x, y), color=(255, 0, 0), thickness=-1)


cv2.namedWindow("image")
cv2.setMouseCallback("image", draw_rectangle)

while True:
    cv2.imshow("image", blank_image)

    # wait 5 seconds then wait for ESC key
    if cv2.waitKey(5) & 0xFF == 27:
        break

cv2.destroyAllWindows()
