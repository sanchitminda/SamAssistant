import os
import numpy
import cv2
facedetect = cv2.CascadeClassifier('Recognizer\\classify_image_graph_def.pb')
cam = cv2.VideoCapture(0)
while True :
    ret, img = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = facedetect.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow('faces',img)
    if cv2.waitKey(1)== 27:
        break
cam.release()
cv2.destroyAllWindows()