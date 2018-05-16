import numpy as np
import cv2
from cv2 import *

pixelBounds = [(80,50), (160,50), (240,50),
               (80,115), (160,115), (240,115),
               (80,195), (160,195), (240,195)
              ]

bounds = [
        ( [15 , 0 , 50] , [35 , 255, 255] , "yellow"),
        ( [100 , 100 , 100] , [150, 255, 255] , "blue"  ),
        ( [60  , 0 , 180] , [140, 100, 255] , "white" ),
        ( [0 , 100 , 50] , [10 , 255, 255] , "orange"),
        ( [70 , 100 , 50] , [100 , 255, 255] , "green" ),
        ( [120, 100 , 50] , [180, 255, 255] , "red"   )
        ]
CUBE = [None]*6
for i in range(1,7):
    impath = "cubePics/Cube"+str(i)+".jpg"
    im = cv2.imread(impath)
    #im = cv2.bilateralFilter(im,9,75,75)
    #im = cv2.fastNlMeansDenoisingColored(im,None,10,10,7,21)
    hsv_img = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)   # HSV image
    Face = [None]*9
 
    for b in bounds:
        lower,upper,color = b
        COLOR_MIN = np.array(b[0],np.uint8)       # HSV color code lower and upper bounds
        COLOR_MAX = np.array(b[1],np.uint8)       #  
        
        frame_threshed = cv2.inRange(hsv_img, COLOR_MIN, COLOR_MAX)     # Thresholding image
        imgray = frame_threshed
        ret,thresh = cv2.threshold(frame_threshed,127,255,0)
        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            x,y,w,h = cv2.boundingRect(cnt)
            
            if(w > 55 and h > 55):
                cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
                for c1,c2 in pixelBounds:
                    midX = range(x,x+w+1)
                    midY = range(y,y+h+1)
                    if(c1 in midX and c2 in midY):
                        index = pixelBounds.index((c1,c2))
                        #print(index)
                        Face[index] = color
               # print(x,y),(x+w,y+h)
        #cv2.imshow("Show",im)
        #cv2.imwrite("extracted.jpg", im)
        #cv2.waitKey()
    print(Face)
    CUBE[i - 1] = Face
cv2.destroyAllWindows()
cubeString = ""
order = []
for face in CUBE:
    blockNum = 1
    for block in face:
        cubeString += str(block)
        if(blockNum == 5):
           order.append(str(block))
        blockNum += 1
print(cubeString)
#URFDLB
cubeString = cubeString.replace(order[0],"U")
cubeString = cubeString.replace(order[1],"R")
cubeString = cubeString.replace(order[2],"F")
cubeString = cubeString.replace(order[3],"D")
cubeString = cubeString.replace(order[4],"L")
cubeString = cubeString.replace(order[5],"B")
import kociemba
print(cubeString)

answer = kociemba.solve(cubeString)
print(answer)
