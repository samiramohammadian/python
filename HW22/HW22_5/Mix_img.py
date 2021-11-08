import cv2
import numpy as np

img1=cv2.imread("lion.jpg",0)
img2=cv2.imread("WhatsApp Image 2021-11-05 at 06.15.29.jpg",0)
new_img1 = cv2.resize ( img1 , (400,400))
new_img2 = cv2.resize ( img2 , (400,400))
r,c = new_img1.shape
print(img1.shape)
print(img2.shape)

img3 = new_img1//2 + new_img2//4
img4 = new_img1//4 + new_img2//2

result =np.zeros ((r*4 , c), dtype="uint8")
result[0:r , 0:c] = new_img1
result[r:r*2 , 0:c] = img3
result[r*2:r*3 , 0:c] = img4
result[r*3:r*4 , 0:c] = new_img2 



cv2.imwrite("result.jpg" , result)
cv2.imshow("photo" , result )
cv2.waitKey()