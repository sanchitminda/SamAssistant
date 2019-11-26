import os
import numpy
import cv2
facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
sampl=0
user_id=input("Enter User ID")
os.mkdir('dataset\\'+user_id)
while True :
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = facedetect.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in face:
        sampl=sampl+1
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.imwrite('dataSet\\'+user_id+'\\'+str(sampl)+'.jpg',gray[y:y+h,x:x+h])
    cv2.imshow('faces', img)
    if cv2.waitKey(100) == 27:
        break
cam.release()
cv2.destroyAllWindows()