import cv2
from numpy.lib.type_check import imag

img1= cv2.imread("1.jpg" , 0)
height1 , width1 = img1.shape
img1 =1-img1
cv2.imwrite('result2_woman.jpg' ,img1)
cv2.imshow( "photo" , img1)
cv2.waitKey()

img2 = cv2.imread("2.jpg" , 0)
height2 , width2 = img2.shape
img2 = 1-img2
cv2.imwrite('result2_man.jpg' ,img2)
cv2.imshow( "photo" , img2) 
cv2.waitKey()
        








  





