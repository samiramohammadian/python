import numpy as np
import cv2

video_cap = cv2.VideoCapture(0)

while True:
    ret,frame = video_cap.read()
    if ret == False:
        break

    frame     = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    point     = frame[200:600 , 450:850]
    mask      = np.ones((51,51))/2601
    result    = cv2.filter2D(frame,-1,mask)

    cv2.rectangle(frame,(453,203), (846,596), (0, 0, 0),6)
    result[200:600 ,450:850] = point
    color_detect_area        = result[200:600 , 450:850]

    if  0 < np.average(color_detect_area) <= 75:
        cv2.putText(result, "BLACK", (25, 50), cv2.FONT_HERSHEY_DUPLEX,1, (0, 0, 0),4) 
    elif 75 < np.average(color_detect_area) <= 125:
        cv2.putText(result, "GRAY", (25, 50), cv2.FONT_HERSHEY_DUPLEX,1, (0, 0, 0),4)
    else:
        cv2.putText(result, "WHITE", (25, 50), cv2.FONT_HERSHEY_DUPLEX,1, (0, 0, 0),4) 

    
    cv2.imshow('result',result)
    cv2.waitKey(1)          
