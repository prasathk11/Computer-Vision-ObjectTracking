import cv2 as cv
import numpy as np

cap=cv.VideoCapture()
ret,first_frame=cv.read()
prev_gray=cv.cvtColor(first_frame,cv.COLOR_BGR2GRAY)

mask=np.zeros_like(frame)
mask[..., 1]=255
while (cap.isOpened()):
    ret, frame = cap.read()
    cv.imshow('input',frame)
    gray = cv.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    flow= cv.calcOpticalFlowFarneback(prev_gray,
                                      gray,
                                      None,
                                      0.5,3,15,3,5,1.2,0)
    magn, angle = cv.cartToPolar((flow[...,0],
                                  flow[...,1]))
    mask[...,2] = cv.normalize(magn,
                               None,
                               0,
                               255,
                               cv.NORM_MINMAX)
    rgb = cv.cvtColor(mask, cv.COLOR_HSV2RGB)
    cv.imshow("Dense Optical Flow",rgb)
    prev_gray = gray
    if cv.waitKey(30) & 0xFF == ord("q"):
        break
cap.release()
cv.destroyAllWindows()