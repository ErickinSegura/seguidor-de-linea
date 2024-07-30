from djitellopy import Tello
import cv2
import numpy as np
from time import sleep

cp = cv2.VideoCapture(0)


hsvVals = [0,107,0,49,255,255]
sensors = 3
thresholdVal = 0.2
width = 360
height = 240

sensibilidad = 3

weights = [-25, -15, 0, 15, 25]
curve = 48
fSpeed = 25



# Inicializar el dron
dr= Tello()
dr.connect()

print("El drone tiene ",dr.get_battery(),"% de bateria")
print("La temperatura del drone es ",dr.get_temperature(),"ºC")

sleep(1)

dr.streamon()
dr.takeoff()

sleep(1)

dr.move_down(67)
def threshold(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower= np.array([hsvVals[0],hsvVals[1],hsvVals[2]])
    upper= np.array([hsvVals[3],hsvVals[4],hsvVals[5]])
    mask= cv2.inRange(hsv, lower, upper)
    return mask

def getContours(imgThres, img):
    contours, hierarchy = cv2.findContours(imgThres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    cx = 0

    if len(contours) != 0:
        biggest = max(contours, key=cv2.contourArea)

        x, y, w, h = cv2.boundingRect(biggest)

        cx= x + w//2
        cy= y + h//2

        cv2.drawContours(img, biggest, -1, (0,0,255), 7)
        cv2.circle(img, (cx,cy), 10, (255,0,0), cv2.FILLED)

    return cx

def getSensors(imgThres, sensors):
    imgs = np.hsplit(imgThres, sensors)
    totalPix = img.shape[1]/sensors * img.shape[0]
    senOut = []
    for x,im in enumerate(imgs):
        pixCount = cv2.countNonZero(im)
        if pixCount > thresholdVal*totalPix:
            senOut.append(1)
        else:
            senOut.append(0)
            
        #cv2.imshow(str(x), im)
    print(senOut)
    return senOut

def commSend(senOut, cx):
    global curve

    #Translacion
    lr = (cx - width//2) // sensibilidad
    lr = int(np.clip(lr, -10, 10))
    
    if lr < 2 and lr > -2:
        lr = 0

    #Rotacion
    if senOut ==   [1,0,0]:
        curve = weights[0]
    elif senOut == [1,1,0]:
        curve = weights[1]
    elif senOut == [0,1,0]:
        curve = weights[2]
    elif senOut == [0,1,1]:
        curve = weights[3]
    elif senOut == [0,0,1]:
        curve = weights[4]
    else:
        curve = weights[2]

    dr.send_rc_control(lr,fSpeed,0,curve)
    


while True:
    #_, img = cp.read()
    img = dr.get_frame_read().frame
    img = cv2.resize(img, (width, height))
    img = cv2.flip(img, 0)

    imgThreshold = threshold(img)
    cx = getContours(imgThreshold, img) #Traslacion en x
    senOut = getSensors(imgThreshold, sensors)

    commSend(senOut, cx)

    #cv2.imshow("Imagen", img)
    #cv2.imshow("Imagen Threshold", imgThreshold)

    cv2.waitKey(1)






