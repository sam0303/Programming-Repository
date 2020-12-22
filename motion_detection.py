import cv2
import numpy as np

cap = cv2.VideoCapture('vtest.avi')
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    diff = cv2.absdiff(frame1,frame2)
    gray =cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20,255,cv2.THRESH_BINARY)
    


    cv2.imshow("inter", frame)

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()