import cv2
import random
import cv2 as cv
import numpy as np

face_detector  = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video_cap  = cv2.VideoCapture(0)

while True:    

    ret, frame = video_cap.read()
    if ret == False:
        break
    
    cv2.putText(frame, "( 1 ) = small blur ", (30, 40), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (255,0,10), 1)
    cv2.putText(frame, "( 2 ) = Big blur ", (30, 70), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (255,0,10), 1)
    cv2.putText(frame, "( 3 ) = new blur ", (30, 100), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (255,0,10), 1)

    key = cv.waitKey(100)

    if ret:

        faces = face_detector.detectMultiScale(frame,1.3)
        
        
        if key == 49: 
            for face in faces:
                x,y,w,h = face
                square  = cv2.resize(frame[y:y+h,x:x+w], (15,15))
            output = cv2.resize(square, (w, h), interpolation=cv2.INTER_NEAREST)
            frame[y:y+h, x:x+h] = output
        elif key == 50:
            for face in faces:
                x,y,w,h = face
                square  = cv2.resize(frame[y:y+h,x:x+w], (8,8))
            output = cv2.resize(square, (w, h), interpolation=cv2.INTER_NEAREST)
            frame[y:y+h, x:x+h] = output
           
        elif key == 51:  
            
            mask = np.ones((10*10)) / 100
            
            for face in faces:
                x, y, w, h = face
                blur = frame[y:y+h,x:x+w]
                result = cv2.filter2D(blur,-1,mask)
                frame[y:y+h,x:x+w] = result
           
            


    
        elif key == 48 :  

            break

            
        cv2.imshow("Advanced Webcam", frame)