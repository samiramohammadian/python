import cv2
import numpy as np
from PIL import Image as im


arr= np.arange(0, 65025 , 1, np.uint8)
img=np.reshape(arr , (255 , 255))
h , w =img.shape

for i in range ( h ):
    for j in range(w):
        img[i][j]=250-i
    

print(img)
cv2.imwrite('part2_6.jpg',img)
cv2.imshow("photo" , img) 
cv2.waitKey()
