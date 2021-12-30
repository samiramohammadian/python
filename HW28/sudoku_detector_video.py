import numpy as np
import cv2
import matplotlib.pyplot as plt
from imutils import contours
from imutils.perspective import four_point_transform

video_cap = cv2.VideoCapture(0)

while True:
    ret,frame = video_cap.read()
    if ret == False:
        break

    cv2.putText(frame, "Press s to save the image ", (30, 70), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (255,0,10), 1)
    cv2.putText(frame, "Press q to Exit", (30, 100), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (255,0,10), 1)
    frame     = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    img_blurred = cv2.GaussianBlur(frame ,(7,7) , 3)
    
    threash = cv2.adaptiveThreshold(img_blurred , 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY_INV , 11 , 2)

    contours = cv2.findContours(threash , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0]

    contours = sorted(contours , key=cv2.contourArea , reverse=True )

    sudoku_contour = None

    for contour in contours :
        #epsilon mizane ddeqate  , msln harchi bod bgm moraba ya na daqiq bashe  
        # 
        epsilon = 0.02 * cv2.arcLength(contour , True)
        approx = cv2.approxPolyDP(contour , epsilon ,True)

        if len(approx) == 4 :
            sudoku_contour = approx 
            break
        
    if sudoku_contour is None:
        print("natonestm peyda konm sudoku ro")

    result = cv2.drawContours(frame ,[sudoku_contour] , -1 , (0,255,0) ,10)

    warped = four_point_transform(frame, approx.reshape(4,2))
    warped = cv2.resize(warped, (500, 500))

    cv2.imshow('cam', frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite(("result.jpg"), warped)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


    cv2.imshow('result',result)
    cv2.waitKey(1)          
