import numpy as np
import cv2

def get_face():
    facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cam = cv2.VideoCapture(0)
    recog = cv2.face.LBPHFaceRecognizer_create()
    recog.read("Recognizer\\trainingData.smfdb")
    idx = 0
    name = ''
    flag = False
    while True:
        ret, img = cam.read()

        if flag:
            break
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        face = facedetect.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in face:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
            flag = True
            idx, conf = recog.predict(gray[y:y + h, x:x + w])

            if(idx==2):
                #print('You are Satyam')
                name = 'Satyam'
            elif(idx == 1):
                #print('you are Sanchit')
                name = 'Sanchit'
            else:
                print(idx)

        cv2.imshow('faces', img)


        if cv2.waitKey(10) == 27:
            break
    cv2.destroyAllWindows()
    cam.release()
    return name

if __name__ == '__main__':
    print(get_face())