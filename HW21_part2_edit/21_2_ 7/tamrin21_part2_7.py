import cv2
import numpy as np
from PIL import Image as im

arr= np.arange(0, 90000, 1, np.uint8)
img=np.reshape(arr , (300 , 300))
h , w =img.shape

img[ : ]=250
t=0 
while(t<130):
    img[t+100:t+120 , 120:180]=0
    t=t+60
    img[120:160 , 100:120]=0
    img[180:220 , 180:200]=0
    img[120:140 , 180:200]=0
    img[200:220 , 100:120]=0


print(img)
cv2.imwrite('part2_7.jpg',img)
cv2.imshow("photo" , img) 
cv2.waitKey()
