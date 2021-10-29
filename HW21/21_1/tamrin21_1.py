import cv2
from numpy.lib.type_check  import imag
from PIL import Image
import numpy as np

w = 800
h = 800
arr=np.zeros((h , w , 1))

for i in range(h):
    for j in range(w):
        x=(i//100)%2
        y=(j//100)%2
        if (x%2 ==0 and y%2==0 ) or (x%2 !=0 and y%2!=0 ):
            arr[i][j]=255
        else:
            arr[i][j]=0
           

print(arr)
cv2.imwrite('result1.jpg',arr)
cv2.imshow("photo" , arr) 
cv2.waitKey()

