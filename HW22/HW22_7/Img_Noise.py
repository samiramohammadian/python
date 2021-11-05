import cv2
import random
import numpy as np

img=cv2.imread("chess pieces.jpg" , 0)
img1=cv2.imread("chess pieces.jpg" , 0)

h ,w =img.shape
d = 1 - 0.025
for i in range(h):
    for j in range(w):
        r = random.random()
        if r < 0.025:
            img[i][j] = 0
        elif r > d:
            img[i][j] = 255
        else:
            img[i][j] = img[i][j]
   

cv2.imwrite("result.jpg" , img)
cv2.imshow("photo" , img)
cv2.waitKey()