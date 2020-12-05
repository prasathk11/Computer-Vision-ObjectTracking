import cv2 as cv
def ask_tracker():
    print("Hi! what tracker API would you like to use ?")
    print("Enter 0 for BOOSTING: ")
    print("Enter 1 for MIL: ")
    print("Enter 2 for KCF: ")
    print("Enter 3 for TLD: ")
    print("Enter 4 for MEDIANFLOW: ")
    print("Enter 5 for GOTURN: ")
    print("Enter 6 for MOSSE: ")
    print("Enter 7 for CSRT: ")

    choice = input('please select your tracker: ')
    if choice == '0':
        tracker = cv.TrackerBoosting_create()
    if choice == '1':
        tracker = cv.TrackerMILcreate()
    if choice == '2':
        tracker = cv.TrackerKCF_create()
    if choice == '3':
        tracker = cv.TrackerTLD_create()
    if choice == '4':
        tracker = cv.TrackerMedianFlow_create()
    if choice == '5':
        tracker = cv.TrackerGOTURN_create()
    if choice == '6':
        tracker = cv.TrackerMOSSE_create()
    if choice == '7':
        tracker = cv.TrackerCSRT_create()
    return tracker


tracker = ask_for_tracker()

tracker_name=str(tracker).split()[0][1:]
cap=cv.VideoCapture('')
ret, frame = cap.read()
roi=cv.selectROI(frame,false)
ret=tracker.init()
while True:
    ret, frame=cap.read()
    success. roi = tracker.update(frame)
    (x,y,w,h)=tuple(map(int, roi))
    if success:
        pts1=(x,y)
        pts2=(x+w, y+h)
        cv.rectangle(frame,pts1,pts2,(255,125,25),3)
    else:
        cv.putText(frame,'Fail to track the object',
                   (100,200),cv.FONT_HERSHEY_SIMPLEX,1,(25,125,255),3)
    cv.putText(frame,tracker_name,(20,400),cv.FONT_HERSHEY_SIMPLEX,1,(255,225,0),3)
    cv.imshow(tracker_name,frame)
    if cv.waitKey(50) & 0xFF == 27:
        break
cap.release()
cv.destroyAllWindows()
