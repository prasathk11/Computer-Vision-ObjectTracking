import cv2 as cv
import numpy as np
#shi-tomasai corner detection
shi_param=dict(maxCorners=30,
               qualityLevel=0.2,
               minDistance=2,
               blockSize=7)
# lucas kande optical flow
lucas_kanade_param=(winSize=(15,15),
                    maxLevel=2,
                    criteria=(cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1))

cap=cv.VideoCapture()
ret,first_frame=cv.read()
prev_gray=cv.cvtColor(first_frame,cv.COLOR_BGR2GRAY)
feat=cv.goodFeaturesToTrack(prev_gray,
                            mask=None,
                            **shi_param)
mask=np.zeros_like(frame)
while(cap.isOpened()):
    ret, frame=cv.read()
    gray_frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    next, status, error = cv.calcOpticalFlowPyrLK(gray_frame,feat,mask=None, **lucas_kanade_param)
    good_old=prev[status==1]
    good_new=next[status==1]
    for i,(new,old) in enumerate(zip(good_new,good_new)):
        a,b = new.ravel()
        c,d = old.ravel()
        mask=cv.line(mask,
                     (a,b),
                     (c,d),
                     color,
                     2)
        frame = cv.Circle(frame,
                          (a,b),
                          (c,d),
                          3,
                          color,
                          -1)
    output=cv.add(frame,mask)
    prev_gray=gray.copy()
    cv.imshow("optical flow",output)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv.destroyAllWindows()