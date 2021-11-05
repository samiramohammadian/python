import cv2

img1=cv2.imread("lion.jpg",0)
img2=cv2.imread("WhatsApp Image 2021-11-05 at 06.15.29.jpg",0)
new_img1 = cv2.resize ( img1 , (400,400))
new_img2 = cv2.resize ( img2 , (400,400))


IMG=  new_img2//2.0  + new_img1//2.0 

cv2.imwrite("result.jpg" , IMG)
cv2.imshow("photo" , IMG )
cv2.waitKey()