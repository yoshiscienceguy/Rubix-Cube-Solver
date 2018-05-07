import numpy
import cv2
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
        print("Ranges")
        print((min(Rrange),max(Rrange)),
              (min(Brange),max(Brange)),
              (min(Grange),max(Grange))
              )
        print(color)
        
        if(color[0] in Rrange and color[1] in Brange and color[2] in Grange):
            self.points.append(point)
            self.blockNumbers.append(block)
            print("winner")
            return True
        return False
font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,500)
fontScale              = 1
fontColor              = (255,255,255)
lineType               = 2


Cube = []
colors = []
ColorNum = 0
for i in range(1,7):
    impath = "cube"+str(i)+".bmp"
    image = cv2.imread(impath)

    image = cv2.resize(image,(300,300))

    #image = cv2.bilateralFilter(image,9,75,75)
    image = cv2.fastNlMeansDenoisingColored(image,None,10,10,7,35)
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


    
    #original = image.copy()
    debug = image.copy()
    
    blockNumber = 1
    
    Face = []
    for length in [50,150,250]:
        for width in [50,150,250]:
            x,y = length,width
            #cv2.circle(debug,(y,x),5,(0,255,0),2)
            #b, g, r = image[x,y,0] , image[x,y,1], image[x,y,2]
            shiftx,shifty = 35,35

            b,g,r = map(int,([image[x-shiftx:x+shiftx,y-shifty:y+shifty, p].mean() for p in range(image.shape[-1])]))
            cv2.rectangle(debug,(y-shifty,x-shiftx), (y+shiftx,x+shiftx),(0,255,0),2)
            print(b,g,r , "BGR")
            match = False
            colormatches = 0
            smooth = 60
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
                        print("*"*80)
                        for existingColor in colors:
                            print(str(existingColor.colorNum) + "!")
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
                        print(b,g,r,cn)
                        if(match):
                            break
                        cv2.waitKey(0)
                        raise Exception("6 Colors Numbers Reached")
                    colors.append(ColorBounds([b,g,r],[x,y],blockNumber,ColorNum))
                    cn = ColorNum
                    break
            print("-"*80)
            cv2.putText(debug,str(cn), (y,x), font, fontScale,fontColor,lineType)
            Face.append(cn)
            print(b,g,r,cn)
            blockNumber += 1
            #cv2.imshow("squares"+str(i),debug)
            #cv2.waitKey(0)
    print(Face)
    Cube.append(Face)
    #cv2.imshow("squares"+str(i),debug)
cubeString = ""
for face in Cube:
    for block in face:
        cubeString += str(block)


cubeString = cubeString.replace("5","U")
cubeString = cubeString.replace("1","R")
cubeString = cubeString.replace("6","F")
cubeString = cubeString.replace("4","D")
cubeString = cubeString.replace("3","L")
cubeString = cubeString.replace("2","B")
import kociemba
print(cubeString)

kociemba.solve(cubeString)


##x,y = 150,50
##cv2.circle(debug,(x,y),5,(0,255,0),2)
##print(image[x,y,0] , image[x,y,1], image[x,y,2])
##x,y = 250,50
##cv2.circle(debug,(x,y),5,(0,255,0),2)
##print(image[x,y,0] , image[x,y,1], image[x,y,2])
##x,y = 50,150
##cv2.circle(debug,(x,y),5,(0,255,0),2)
##print(image[x,y,0] , image[x,y,1], image[x,y,2])
##x,y = 150,150
##cv2.circle(debug,(x,y),5,(0,255,0),2)
##print(image[x,y,0] , image[x,y,1], image[x,y,2])
##x,y = 250,150
##cv2.circle(debug,(x,y),5,(0,255,0),2)
##print(image[x,y,0] , image[x,y,1], image[x,y,2])
##x,y = 50,250
##cv2.circle(debug,(x,y),5,(0,255,0),2)
##print(image[x,y,0] , image[x,y,1], image[x,y,2])
##x,y = 150,250
##cv2.circle(debug,(x,y),5,(0,255,0),2)
##print(image[x,y,0] , image[x,y,1], image[x,y,2])
##x,y = 250,250
##cv2.circle(debug,(x,y),5,(0,255,0),2)
##print(image[x,y,0] , image[x,y,1], image[x,y,2])
##cv2.imshow("squares",debug)



##
####
####image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
##
##boundaries = [
##    ([255, 255, 255], [255, 255, 255],  "white"),
##    ([0, 255, 255], [1, 255, 255],  "yellow"),
##    ([0, 153, 255], [0, 153, 255],  "orange"),
##    ([250, 0, 0], [255, 0, 0],  "blue"),
##    ([0, 200, 0], [1, 255, 1],  "green"),
##    ([0, 0, 250], [10, 10, 255], "red")
##        
##]
##for color in boundaries:
##    lower,upper,name = color
##    
##    lower = numpy.array(lower, dtype = numpy.uint8)
##    upper = numpy.array(upper, dtype = numpy.uint8)
##    
##    mask = cv2.inRange(original,lower,upper)
##    kernelOpen=numpy.ones((5,5))
##    kernelClose=numpy.ones((20,20))
##    maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
##    maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)
##    
##    #ret,thresh = cv2.threshold(mask,r,g,b)
##    conts, hierarchy = cv2.findContours(maskClose,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
##
##    cv2.drawContours(image,conts,-1,(255,0,0),3)
##    for i in range(len(conts)):
##        x,y,w,h=cv2.boundingRect(conts[i])
##        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255), 2)
##
##    cv2.imshow(name,mask)
##    cv2.imshow("altered",image)
##    cv2.imshow("original",original)
##    cv2.waitKey(0)
cv2.waitKey(0)
cv2.destroyAllWindows()
