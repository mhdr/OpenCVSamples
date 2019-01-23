import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID') # specify the codec
out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while True:
    ret, frame = cap.read()
    cv2.imshow("frame", frame)
    out.write(frame)

    # exit video capture
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
