import cv2
import numpy as np 

img    = cv2.imread("flower_input.jpg" , 0)
result = np.zeros(img.shape)
mask   = np.ones((51 ,51)) / 2601
rows , cols = img.shape

for i in range(25,rows-25):
    for j in range(25,cols-25):
        if img[i][j] < 130  :
            small_img = img[i-25:i+26 , j-25:j+26]
            result[i ,j] = np.sum (small_img * mask)
        else :
            result [i,j] = img[i][j]

cv2.imwrite("result.jpg" , result)



