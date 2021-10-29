import cv2

img=cv2.imread('4.jpg' , 0 )


h ,w =img.shape
for i in range(h):
    for j in range(w):
        if img[i][j]<100 :
            img[i][j]=0


cv2.imwrite('result4.jpg',img)
cv2.imshow("photo" ,img) 
cv2.waitKey()

