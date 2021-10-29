import cv2

img=cv2.imread('5.jpeg' , 0 )


h ,w =img.shape
i=50
j=0
while i+31>0:
    k=0
    while k<31:
        if i+k>0:
            img[j][i+k]=0
        k=k+1
    i=i-1
    j=j+1

cv2.imwrite('result5.jpg',img)
cv2.imshow("photo" ,img) 
cv2.waitKey()

