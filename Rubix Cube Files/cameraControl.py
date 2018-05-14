import numpy as np
import cv2
import time

def ProcessPic(cap):
    # Capture frame-by-frame
    ret, frame = cap.read()

    crop = frame[0:500,100:570]
    # Display the resulting frame
    return crop

def takePicture(picNum):
    cap = cv2.VideoCapture(0)
    picture = ProcessPic(cap)
    fileName = "./cubePics/Cube"+str(picNum)+".jpg"
    print("Picture Taken: "+fileName)
    cv2.imwrite(fileName, picture)
    del(cap)

def testCamera():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow("cam",frame)
        if(cv2.waitKey(1) == 27):
           break
    cv2.destroyAllWindows()


