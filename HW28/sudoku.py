import cv2
import matplotlib.pyplot as plt
from imutils.perspective import four_point_transform 
import argparse

parser = argparse.ArgumentParser(description = "samira sudoku ")
parser.add_argument("--input" , type=str , help = "path of your input imgae")
parser.add_argument("--output" , type=str , help = "size of GaussianBlur mask")
parser.add_argument("--filter-size" , type=str , help = "path of your output imgae")

args = parser.parse_args()

img = cv2.imread(args.input )
img_gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
img_blurred = cv2.GaussianBlur(img_gray ,(args.filter_size , args.filter_size) , 3)
threash = cv2.adaptiveThreshold(img_blurred , 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY_INV , 11 , 2)
#threash = cv2.bitwise_not(threash)  #thresh binary_inv ==


contours = cv2.findContours(threash , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0]

contours = sorted(contours , key=cv2.contourArea , reverse=True )

sudoku_contour = None

for contour in contours :
    #epsilon mizane ddeqate  , msln harchi bod bgm moraba ya na daqiq bashe  
    # 
    epsilon = 0.1 * cv2.arcLength(contour , True)
    approx = cv2.approxPolyDP(contour , epsilon ,True)

    if len(approx) == 4 :
       sudoku_contour = approx 
       break
       
if sudoku_contour is None:
    print("natonestm peyda konm sudoku ro")


result = cv2.drawContours(img ,[sudoku_contour] , -1 , (0,255,0) ,10)


crop = four_point_transform(img, approx.reshape(4,2))
crop = cv2.resize(crop, (500, 500))
plt.imshow(crop)
cv2.imwrite(args.output , crop)

