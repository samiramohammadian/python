import cv2

img1 = cv2.imread("board - origin.bmp",0)
img2 = cv2.imread("board - test.bmp",0)


new_img2=cv2.flip(img2, 1)

IMG = cv2.subtract(img1 ,new_img2 )
result= IMG *255
h,w= result.shape
for i in range(h):
    for j in range(w):
        if result[i][j]< 0 :
            result[i][j] =0

        elif result[i][j]>255 :
            result[i][j]=255
        else :
            result[i][j]=result[i][j]

cv2.imwrite("result.jpg" , result )
cv2.imshow("photo" , IMG )
cv2.waitKey()