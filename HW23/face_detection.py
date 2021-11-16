import cv2
import random
import cvzone
import cv2 as cv

def menu():
    text1 = " ( 1 ) = \n ( 2 ) = \n ( 3 ) = \n ( 4 ) = \n ( 0 ) ="
    text2 = " Emoji on Face \n Emoji on eyes & lips \n Pixelate Face \n Reverse Face \n Quit"
    y0  , dy  = 20, 50
    y02 , dy2 = 20 ,50
    for i, line in enumerate (text1.split('\n')):
        y = y0 + i*dy
        cv2.putText(frame, line, (2 , y ), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1 , (10 , 0 , 255), 2)
 
    for i, line in enumerate(text2.split('\n')):
        y2= y02 + i*dy2
        cv2.putText(frame, line, (100 , y2 ), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1 , (0 , 0 , 0), 2)


sticker1    = cv2.imread("emoji1.png" ,cv2.IMREAD_UNCHANGED)
sticker2    = cv2.imread("emoji2.png" ,cv2.IMREAD_UNCHANGED)
sticker3    = cv2.imread("emoji3.png" ,cv2.IMREAD_UNCHANGED)
sticker4    = cv2.imread("emoji4.png" ,cv2.IMREAD_UNCHANGED)
sticker5    = cv2.imread("emoji5.png" ,cv2.IMREAD_UNCHANGED)
sticker_eye = cv2.imread("eye.png"    ,cv2.IMREAD_UNCHANGED)
sticker_lips= cv2.imread("smile.png"  ,cv2.IMREAD_UNCHANGED)
stickers    = [sticker1 , sticker2 , sticker3 , sticker4 , sticker5]

face_detector  = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_detector   = cv2.CascadeClassifier(   "haarcascade_eye.xml"             )
smile_detector = cv2.CascadeClassifier(  "haarcascade_smile.xml"            )

video_cap  = cv2.VideoCapture(0)

while True:    

    ret, frame = video_cap.read()
    if ret == False:
        break
    
    menu()
    key = cv.waitKey(100)

    if ret:

        faces = face_detector.detectMultiScale(frame,1.3)
        eyes  = eye_detector.detectMultiScale(frame, 1.1, maxSize=(70 , 70))  
        lips  = smile_detector.detectMultiScale(frame,1.34, 29) 
        
        if key == 49: 

            for face in faces:
                x,y,w,h = face
                sticker_resized = cv2.resize(random.choice(stickers), (w, h))
                frame = cvzone.overlayPNG(frame, sticker_resized, [x, y])


        elif key == 50:
            
            for eye in eyes:
                xe,ye,we,he = eye
                sticker_resized = cv2.resize(sticker_eye, (we, he))
                frame = cvzone.overlayPNG(frame, sticker_resized, [xe, ye])
            
            for lip in lips:
                xl,yl,wl,hl = lip
                sticker_resized = cv2.resize(sticker_lips, (wl, hl))
                frame = cvzone.overlayPNG(frame, sticker_resized, [xl, yl])


        elif key == 51:  
            
            cv2.putText(frame, "( 8 ) = Small", (290, 110), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (255,0,10), 1)
            cv2.putText(frame, "( 9 ) = Big  ", (290, 130), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (255,0,10), 1)

    
        elif key == 56 :

            for face in faces:
                x,y,w,h = face
                square  = cv2.resize(frame[y:y+h,x:x+w], (15,15))
            output = cv2.resize(square, (w, h), interpolation=cv2.INTER_NEAREST)
            frame[y:y+h, x:x+h] = output


        elif key == 57 :

            for face in faces:
                x,y,w,h = face
                square  = cv2.resize(frame[y:y+h,x:x+w], (8,8))
            output = cv2.resize(square, (w, h), interpolation=cv2.INTER_NEAREST)
            frame[y:y+h, x:x+h] = output


        elif key == 52:

            for face in faces:
                x,y,w,h = face
                frame[y:y+h, x:x+h] = cv2.rotate(frame[y:y+h, x:x+h], cv2.ROTATE_180)

        elif key == 48 :  

            break
 


        else:

            pass
        

        cv2.imshow("Advanced Webcam", frame)