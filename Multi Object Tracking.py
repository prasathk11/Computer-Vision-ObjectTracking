import  cv2 as cv
import sys
from random import randint

tracker_types=['BOOSTING',
               'MIL',
               'TLD',
               'MEADIANFLOW',
               'GOTURN',
               'MOSSE',
               'CSRT']
def tracker_name(tracker_type):
    if tracker_type==tracker_types[0]:
        tracker = cv.TrackerBoosting_create()
    elif tracker_type==tracker_types[1]:
        tracker = cv.TrackerBoosting_create()
    elif tracker_type==tracker_types[2]:
        tracker = cv.TrackerBoosting_create()
    elif tracker_type==tracker_types[3]:
        tracker = cv.TrackerBoosting_create()
    elif tracker_type==tracker_types[4]:
        tracker = cv.TrackerBoosting_create()
    elif tracker_type==tracker_types[5]:
        tracker = cv.TrackerBoosting_create()
    elif tracker_type==tracker_types[6]:
        tracker = cv.TrackerBoosting_create()
    elif tracker_type==tracker_types[7]:
        tracker = cv.TrackerBoosting_create()
    else:
        tracker=None
        print('No tracker found')
        print('Choose from these trackers: ')
        for tr in tracker_types:
            print(tr)
    return tracker
if __name__== '__main__':
    print("Default tracking algorithm MOSSE \n"
          "Available algorithms are: \n")
    for tr in tracker_types:
        print(tr)
    tracker_types = 'MOSSE'

    cap = cv.VideoCapture('E:\AI projects\Opencv\Videos\kitten.mp4')
    success, frame = cap.read()
    if not success:
        print('Cannot read the video')
    rects=[]
    colors=[]
    while True:
        rect_box = cv.selectROI('MultiTracker',frame)
        rects.append(rect_box)
        colors.append((randint(64,255),randint(64,255),randint(64,255)))
        print('Press q to stop selecting boxes and start multitracking')
        print('Press any key to select another box')
        if cv.waitkey(0) & 0xFF == ord('q'):
            break

    print(f'Selected boxes {rects}')
    multitracker = cv.MultiTracker_create()
    for rect_box in rects:
        multitracker.add(tracker_name(tracker_types),
                         frame, rect_box)
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        success, boxes = multitracker.update(frame)

        for i, newbox in enumerate(boxes):
            pts1 = (int(newbox[0]),int(newbox[1]))
            pts2 = (int(newbox[0] + newbox[2]),
                    int(newbox[1] + newbox[3]))
            cv.rectangle(frame, pts1, pts2, colors[i],2,1)
        cv.imshow('Multitracker',frame)
        if cv.waitKey(0) & 0xFF == ord('q'):
            break
cap.release()
cv.destroyAllWindows()


