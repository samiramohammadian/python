import cv2

img1 = cv2.imread ( "a.tif" , 0)
img2 = cv2.imread ( "b.tif" , 0)

IMG = img2 - img1 

cv2.imwrite("result.jpg" , IMG)
cv2.imshow("photo",IMG)

cv2.waitKey()