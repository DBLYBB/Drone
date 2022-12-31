import cv2
import time
import serial
import numpy as np
from FlightController.Solutions.Vision_Net import FastestDetOnnx, FastestDet


deep = FastestDetOnnx(drawOutput=False)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640.0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640.0)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))

while True:
    img = cap.read()[1]
    if img is None:
        continue
    #cv2.imshow("Origin", img)
    get = deep.detect(img)
    print(get)
    #cv2.imshow("Result", img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord ("q"):
        break
        cv2.destroyAllWindows()