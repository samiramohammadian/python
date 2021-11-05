import cv2

img = cv2.imread("Mona_Lisa.jpg" , 0)

inverted = 255 - img
blurred = cv2.GaussianBlur(inverted , (21,21) , 0 ) #tasvir ra mat va tar mikonad va sefid 
inverted_blurred = 255 - blurred                    #rang tasvir ra be halat aval bar migardanad ama ba haman halat tar o mat


sketch = img / inverted_blurred
cv2.imshow("photo" , sketch )

sketch = sketch*255

cv2.imwrite ("result.jpg" , sketch)
cv2.waitKey()