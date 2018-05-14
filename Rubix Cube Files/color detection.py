import numpy
import cv2
import time
import threading
start = time.time()
print("Start Time: "+str(start))
class ColorBounds():
    def __init__(self,u,point,block,cn):
        self.detectedColor = u
        self.points = [point]
        self.blockNumbers = [block]
        self.colorNum = cn
    def fit(self,color,point,block,smooth):
        color = [numpy.clip(color[0],0,255),numpy.clip(color[1],0,255),numpy.clip(color[2],0,255)]
        Rrange = list(set(numpy.clip(range(self.detectedColor[0] - smooth, self.detectedColor[0] + smooth),0,255)))
        Brange = list(set(numpy.clip(range(self.detectedColor[1] - smooth , self.detectedColor[1] + smooth),0,255)))
        Grange = list(set(numpy.clip(range(self.detectedColor[2] - smooth , self.detectedColor[2] + smooth),0,255)))
##        print("Ranges")
##        print((min(Rrange),max(Rrange)),
##              (min(Brange),max(Brange)),
##              (min(Grange),max(Grange))
##              )
##        print(color)
        
        if(color[0] in Rrange and color[1] in Brange and color[2] in Grange):
            self.points.append(point)
            self.blockNumbers.append(block)
            #print("winner")
            return True
        return False


def processImage(picNum):
    
    impath = "./cubePics/Cube"+str(picNum)+".jpg"
    image = cv2.imread(impath)
    image = image[10:430,30:450]
    image = cv2.resize(image,(300,300))

    #image = cv2.bilateralFilter(image,9,75,75)
    #image = cv2.fastNlMeansDenoisingColored(image,None,10,10,7,35)
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    images[picNum - 1] = image
    #cv2.imshow("squares",image)
    #cv2.waitKey(0)

def getColor(image):
    global colors, ColorNum,Cube
    
    #original = image.copy()
    debug = image.copy()

    blockNumber = 1
    
    Face = []
    for length in [50,150,250]:
        for width in [50,150,250]:
            x,y = length,width
            #cv2.circle(debug,(y,x),5,(0,255,0),2)
            #b, g, r = image[x,y,0] , image[x,y,1], image[x,y,2]
            shiftx,shifty = 20,20

            b,g,r = map(int,([image[x-shiftx:x+shiftx,y-shifty:y+shifty, p].mean() for p in range(image.shape[-1])]))
            cv2.rectangle(debug,(y-shifty,x-shiftx), (y+shiftx,x+shiftx),(0,255,0),2)
            print(b,g,r , "BGR")
            match = False
            colormatches = 0
            smooth = 40
            while colormatches != 1:
                
                for existingColor in colors:
                    if(existingColor.fit([b,g,r],[x,y],blockNumber,smooth)):
                        match = True
                        cn = existingColor.colorNum
                        colormatches += 1

                #print(colormatches,match)
                if(colormatches > 1):
                    smooth -= 5
                    if(smooth < 0):
                        raise Exception("Reached Negative")
                    colormatches = 0
                    match = False
                    continue
                if(not match):
                    ColorNum += 1
                    if(ColorNum > 6):
                        #print("*"*80)
                        for existingColor in colors:
                            #print(str(existingColor.colorNum) + "!")
                            if(existingColor.fit([b+25,g+25,r+25],[x,y],blockNumber,50)):
                                match = True
                                cn = existingColor.colorNum
                                colormatches += 1
                                break
                            elif(existingColor.fit([b-25,g-25,r-25],[x,y],blockNumber,65)):
                                match = True
                                cn = existingColor.colorNum
                                colormatches += 1
                                break
                        #print(b,g,r,cn)
                        if(match):
                            break
                        cv2.waitKey(0)
                        raise Exception("6 Colors Numbers Reached")
                    colors.append(ColorBounds([b,g,r],[x,y],blockNumber,ColorNum))
                    cn = ColorNum
                    break
            #print("-"*80)
            cv2.putText(debug,str(cn), (y,x), font, fontScale,fontColor,lineType)
            Face.append(cn)
            #print(b,g,r,cn)
            blockNumber += 1
    cv2.imshow("squares"+str(i),debug)
    #cv2.waitKey(0)
    print("Processed Face. Result: " + str(Face))
    return Face

font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,500)
fontScale              = 1
fontColor              = (255,255,255)
lineType               = 2


Cube = [[],[],[],[],[],[]]
images = [[],[],[],[],[],[]]
colors = []
ColorNum = 0
threads = []

for i in range(1,7):
    
    t = threading.Thread(target = processImage, args=(i,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
end = time.time()
print("End time: "+ str(end))
total = end - start
minutes = str(round(total / 60))
seconds = str(round(total%60,2))
print("Total time: "+  minutes + " , " + seconds + " seconds")
for i in range(6):
    Face = getColor(images[i])
    Cube[i] = Face
    #cv2.imshow("squares"+str(i),debug)
    #cv2.waitKey(0)
    
cubeString = ""
order = []
for face in Cube:
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
end = time.time()
print("End time: "+ str(end))
total = end - start
minutes = str(round(total / 60))
seconds = str(round(total%60,2))
print("Total time: "+  minutes + " , " + seconds + " seconds")
cv2.waitKey(0)
cv2.destroyAllWindows()
