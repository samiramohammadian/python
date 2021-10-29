import cv2
import numpy as np

new_img=cv2.imread('3.jpg' ,0 )
#new_img=cv2.resize(img,(300,400))

h ,w =new_img.shape
img2=cv2.imread('3.jpg' ,0 )
#new_img=cv2.resize(img2,(300,400))
h1=0
w1=0

for i in range( h-1 , 0,-1  ):
    w1=0
    for j in range( w-1 , 0,-1 ):
        
        img2[h1][w1]=new_img[i][j]
      

        w1=w1+1
    h1=h1+1    


cv2.imwrite('result3.jpg',img2)
cv2.imshow("photo" ,img2) 
cv2.waitKey()




