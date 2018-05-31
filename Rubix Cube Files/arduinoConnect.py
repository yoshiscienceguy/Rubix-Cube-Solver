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
def sendString(answer):
        s = answer
        s = s.replace("2","Q")
        s = s.replace("'","W")
        s = s.replace("R","2")
        s = s.replace("L","3")
        s = s.replace("U","4")
        s = s.replace("D","5")
        s = s.replace("B","6")
        s = s.replace("F","7")
        stringToSend = s.split(" ")
        
        packet = []
        for letter in stringToSend:
                info = ["","0"]
                if("W" in letter):
                        info[1] = "1"
                        info[0] = letter[0]
                if('Q' in letter):
                        info[0] = letter[0]
                        for i in range(2):
                                packet.append(info)
                else:
                        info[0] = letter[0]
                        packet.append(info)
        ser = serial.Serial('/dev/ttyACM0',9600)
        time.sleep(5)
        print(str(len(packet)) + " moves" )
        moveNum = 0
        for letter,reverse in packet:
                print(str(moveNum) + "/" + str(len(packet)))
                moveNum += 1
                ser.write((letter+"/r/n").encode())
                ser.write((reverse+"/r/n").encode())
                while True:
                        data = ser.readline()
                        data = data.strip()
                        if(data == "done"):
                                break
                
        ser.write(str(8).encode())       
        
##        ser.write("2\r\n".encode())
##        ser.write((str(len(stringToSend)) + "\r\n").encode())
##        time.sleep(.1)
##        for a in stringToSend:
##                print(a)
##                ser.write((a+"\r\n").encode())
