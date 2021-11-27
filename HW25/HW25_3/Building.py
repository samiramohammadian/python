import cv2
import numpy as np 

img    = cv2.imread("building.tif" , 0)
img1   = cv2.imread("building.tif" , 0)
result = np.zeros(img.shape)
result1= np.zeros(img.shape)
mask   = np.array([[-1 , 0 , 1],
                  [-1 , 0 , 1],
                  [-1 , 0 , 1]] )

mask1  = np.array([[-1 , -1 , -1],
                   [0 , 0 , 0],
                   [1 , 1 , 1]] )

rows , cols = img.shape

for i in range(1,rows-1):
    for j in range(1,cols-1):
        small_img = img[i-1:i+2 , j-1:j+2]
        result[i ,j] = np.sum (small_img * mask)
        small_img1 = img1[i-1:i+2 , j-1:j+2]
        result1[i ,j] = np.sum (small_img1 * mask1)
    

cv2.imwrite("result1.jpg" , result)
cv2.imwrite("result2.jpg" , result1)

