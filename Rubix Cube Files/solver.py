import numpy as np
import cv2
from cv2 import *
import kociemba
import arduinoConnect

pixelBounds = [(80,50), (160,50), (240,50),
               (80,115), (160,115), (240,115),
               (80,195), (160,195), (240,195)
              ]

bounds = [
        ( [15 , 0 , 50] , [35 , 255, 255] , "yellow"),
        ( [100 , 100 , 100] , [150, 255, 255] , "blue"  ),
        ( [100  , 0 , 180] , [150, 180, 255] , "white" ),
        ( [6 , 100 , 50] , [15 , 255, 255] , "orange"),
        ( [35 , 100 , 50] , [80 , 255, 255] , "green" ),
        ( [120, 100 , 50] , [180, 255, 255] , "red"   ),
        ( [0, 100 , 50] , [5, 255, 255] , "red"   ),
        ]
CUBE = []

def makeCube():
    global CUBE
    
    for i in range(1,7):
        impath = "./cubePics/Cube"+str(i)+".jpg"
        im = cv2.imread(impath)

        #im = cv2.bilateralFilter(im,9,75,75)
        #im = cv2.fastNlMeansDenoisingColored(im,None,10,10,7,21)
        hsv_img = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)   # HSV image
        Face = []
     
        for b in bounds:
            lower,upper,color = b
            COLOR_MIN = np.array(b[0],np.uint8)       # HSV color code lower and upper bounds
            COLOR_MAX = np.array(b[1],np.uint8)       #  
            
            frame_threshed = cv2.inRange(hsv_img, COLOR_MIN, COLOR_MAX)     # Thresholding image
            imgray = frame_threshed
            ret,thresh = cv2.threshold(frame_threshed,127,255,0)
            _,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

            for cnt in contours:
                x,y,w,h = cv2.boundingRect(cnt)
                
                if(w > 50 and h > 50):
                    cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
                    point = [(x,y),(x+w,y+h),color]
                    midx,midy = x + w/2, y + h/2
                    if(len(Face) > 0):
                        found = False
                        for p1,p2,_ in Face:
                            x1,y1 = p1
                            x2,y2 = p2
                            if(midx >= x1 and midx <= x2):
                                if( midy >= y1 and midy <= y2):
                                    found = True
                                    break
                        if(not found):
                            Face.append(point)
                    else:
                        Face.append(point)
            cv2.imshow("Show",im)
    
            cv2.waitKey()
        #print(len(Face))
        #print(Face)
        colorface = []
        facePoints = []
        for point1,point2,color in Face:
            facePoints.append([point1[0],point1[1],color])
            
        orderedY = sorted(facePoints, key = lambda k: [k[1],k[0]])
        
        top = orderedY[:3]
        orderedX = sorted(top, key = lambda k: [k[0],k[1]])
        for Xcoor, yCoor, color in orderedX:
            colorface.append(color)

        middle = orderedY[3:6]
        orderedX = sorted(middle, key = lambda k: [k[0],k[1]])
        for Xcoor, yCoor, color in orderedX:
            colorface.append(color)

        low = orderedY[6:9]
        orderedX = sorted(low, key = lambda k: [k[0],k[1]])
        for Xcoor, yCoor, color in orderedX:
            colorface.append(color)
        print(colorface)
        CUBE.append(colorface)
        #cv2.imshow("Show",im)   
        cv2.waitKey()
    cv2.destroyAllWindows()

def Solve():
    cubeString = ""
    order = []
    for face in CUBE:
        blockNum = 1
        for block in face:
            cubeString += str(block)
            if(blockNum == 5):
               order.append(str(block))
            blockNum += 1
    #print(cubeString)
    #URFDLB
    cubeString = cubeString.replace(order[0],"U")
    cubeString = cubeString.replace(order[1],"R")
    cubeString = cubeString.replace(order[2],"F")
    cubeString = cubeString.replace(order[3],"D")
    cubeString = cubeString.replace(order[4],"L")
    cubeString = cubeString.replace(order[5],"B")
    
    return(cubeString)


arduinoConnect.startScan()

makeCube()
cs = Solve()
answer = kociemba.solve(cs)
print(answer)
arduinoConnect.sendString(answer)
