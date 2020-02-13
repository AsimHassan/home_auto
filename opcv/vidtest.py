import numpy as np 
import cv2,PIL
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl 
aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)

##cap = cv2.VideoCapture('tv1.mov')
cap = cv2.VideoCapture('http://172.20.10.4:8080/?action=stream')
parameters =  aruco.DetectorParameters_create()
i=0
while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret,thresh2 = cv2.threshold(gray,200,255,cv2.THRESH_BINARY)
    
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    ##cv2.imshow('ar1',thresh2)
    ##frame_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)
    ##cv2.imshow('ar',frame_markers)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if(ids is not None):
        print(ids)
        print(i)
        i=i+1

cap.release()
cv2.destroyAllWindows()