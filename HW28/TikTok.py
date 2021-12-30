import numpy as np
import cv2

video_cap = cv2.VideoCapture(0)
ar = []
row = 1

while True:
    ret,frame = video_cap.read()
    if ret == False :
        break
  
  
    if ret:

        rows , cols , _   = frame.shape

        if row <= rows: 
            ar.append(frame[row-1])
            frame[:row , :] = np.array(ar)
            cv2.line(frame, (0, row), (cols, row), (0,255,0), 1)
            row = row+1

        elif row > rows :
            break

        cv2.imshow("output!", frame)
        cv2.waitKey(1)

