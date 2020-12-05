import cv2 as cv
import numpy as np

cap = cv.VideoCapture()
ret, frame = cap.read()

face_cascade = cv.CascadeClassifier('')
face_rects = face_cascade.detectMultiScale(frame)

x,y,w,h=tuple(face_rects[0])
track_window = (x ,y , w , h)
roi = frame[x:y+h,
            x:x+w]

hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)

roi_hist = cv.calcHist([hsv_roi,
                        [0],
                        None,
                        [180],
                        [0,180]])
cv.normalize(roi_hist,roi_hist,0 ,255, cv.NORM_MINIMAX);
term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10 , 1)
while True:
    ret, frame = cap.read()
    if ret == True:
        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        dest_roi = cv.calcBackProject([hsv],[0],roi_hist,[0,180],1)
        ret, track_window = cv.meanShift(dest_roi,track_window,term_crit)
        pts = cv.boxPoints(ret)
        pts = np.int0(pts)
        img2=cv.polylines(frame,[pts],True,(0,255,0),5)
        cv.imshow('Cam Shift',img2)
        if cv.waitKey(0) & 0xFF == ord('q'):
            break
        else:
            break
cap.release()
cv.destroyAllWindows()