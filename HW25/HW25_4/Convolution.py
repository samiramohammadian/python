from typing import ValuesView
import cv2
import numpy as np 

def convolution (img , value ):
    mask   = np.ones((value , value)) / value **2 
    result = np.zeros(img.shape)
    rows , cols = img.shape
    for i in range(value //2 ,rows-(value //2)):
        for j in range(value//2 ,cols-(value // 2 )):
            small_img = img[i-(value//2):i+1+(value//2) ,j-(value//2):j+1+(value//2)]
            result[i ,j] = np.sum (small_img * mask)
    cv2.imwrite("result.jpg" , result)

img    = cv2.imread("car.jpeg" , 0)
while True:
    print(" chooise the value \n ")
    print(" 1. 3*3 ")
    print(" 2. 5*5")
    print(" 3. 7*7 ")
    print(" 4. 15*15 ")
    option = int(input() )
    if option==1:
        convolution(img , 3)
        break
    if option==2:
        convolution(img , 5)
        break
    if option==3:
        convolution(img , 7)
        break
    if option==4:
        convolution(img , 15)
        break
    else:
        print("wrong!!!!!")
        break






