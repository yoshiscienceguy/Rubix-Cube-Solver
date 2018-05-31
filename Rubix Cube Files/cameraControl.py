import numpy as np
import cv2
import time
import urllib
from imutils.video import VideoStream
import imutils

def ProcessPic(cap):
    # Capture frame-by-frame
    #ret, frame = cap.read()

    crop = cap[185:485,230:530]
    # Display the resulting frame
    return crop

def takePicture(picNum):
    frameSize = (800, 608)

    vs = VideoStream(src=0, usePiCamera=True, resolution=frameSize,
                framerate=32).start()
    time.sleep(.5)

    cap = vs.read()
    picture = ProcessPic(cap)
    fileName = "./cubePics/Cube"+str(picNum)+".jpg"
    print("Picture Taken: "+fileName)
    cv2.imwrite(fileName, picture)
    vs.stop()
def testCamera():
    #cap = cv2.VideoCapture(1)
    frameSize = (800, 608)

    vs = VideoStream(src=0, usePiCamera=True, resolution=frameSize,
                framerate=32).start()
    time.sleep(.5)
    while True:
        frame = vs.read()

        # If using a webcam instead of the Pi Camera,
        # we take the extra step to change frame size.
        if not True:
                frame = imutils.resize(frame, width=frameSize[0])
        picture = ProcessPic(frame)
        cv2.imshow("cam",picture)

        if(cv2.waitKey(1) == 27):
           break
    cv2.destroyAllWindows()


