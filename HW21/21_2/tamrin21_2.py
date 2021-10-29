import cv2
from numpy.lib.type_check import imag

def inv(img ,height , width):  
    i=0  
    while (i<height) :
        j=0
        while (j<width) :
            img[i][j]= 255-img[i][j]
            j=j+1
        i=i+1  

while True:
    print("gozine ra vared konud: \n")
    print("1. image1 : \n")
    print("2. image2 : \n")
    x=int(input())
    if x==1:
        img1= cv2.imread("1.jpg" , 0)
        

        height1 , width1 = img1.shape
        inv(img1 , height1 ,width1 ) 
        cv2.imwrite('result2_woman.jpg' ,img1)
        cv2.imshow( "photo" , img1)
        cv2.waitKey()
        break


    elif x==2:
        img2 = cv2.imread("2.jpg" , 0)
        

        height2 , width2 = img2.shape
        inv(img2 , height2 ,width2 ) 
        cv2.imwrite('result2_man.jpg' ,img2)
        cv2.imshow( "photo" , img2) 
        cv2.waitKey()
        break
    
    else :
        print("gozine dorost ra vared nakardid .")
        break









  





