import numpy as np
import cv2
import os

def openWebcam():
    capture = cv2.VideoCapture(0)
    while(True):
        #capture frame by frame
        ret, frame = capture.read()
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        # show my video here
        cv2.imshow('My Webcam', gray)
        if cv2.waitKey(0):
            break
    capture.release()
    cv2.destroyAllWindows()

def capPhoto():
    capture = cv2.VideoCapture(0)
    ret, img = capture.read()
    os.chdir('C:/gitclone/Django/openwebcam/webcam/static/webcam/images/')
    cv2.imwrite('capture.jpg', img)
    capture.release()
    cv2.destroyAllWindows()