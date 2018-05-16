import serial
import time
from cameraControl import *

def startScan():
        ser = serial.Serial('/dev/ttyACM0',9600)
        time.sleep(2)
        ser.write("1")
        names = [5,6,2,3,4,1]
        picNum = 0
        while picNum < 6:
                data = ser.readline()
                data = data.strip()
                if(data == "done"):
                        print(picNum)
                        takePicture(names[picNum])
                        picNum += 1
                
def cameraDebug():
        testCamera()
