import cv2
import numpy as np

images = []
for i in range(1,15):
    img=cv2.imread(f"h{i}.jpg" , 0)
    images.append(img)
    rows , cols = img.shape

IMG = np.zeros (( rows , cols ) , dtype ="uint8")

for image in images :
    IMG+=image//14
cv2.imwrite( "resuli.jpg" , IMG)
cv2.imshow( "photo" , IMG)
cv2.waitKey()