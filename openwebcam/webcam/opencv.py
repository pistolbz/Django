import numpy as np
import cv2
import os
import time

def openWebcam():
    capture = cv2.VideoCapture(0)
    time_begin = time.localtime()[5]
    while(True):
        #capture frame by frame
        ret, frame = capture.read()
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        # show my video here
        cv2.imshow('My Webcam', gray)
        if cv2.waitKey(0) or time_begin + 5 == time.localtime()[5]:
            break
    capture.release()
    cv2.destroyAllWindows()

def capPhoto():
    capture = cv2.VideoCapture(0)
    ret, img = capture.read()
    cv2.imwrite('../static/img/capture.jpg', img)
    capture.release()
    cv2.destroyAllWindows()