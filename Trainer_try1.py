import numpy as np
import os
from PIL import Image
import cv2
import cv2.face as cf
imgpth='dataSet'
recog = cv2.face.LBPHFaceRecognizer_create()
fout = open('Id_List.dat','w')
def getImagesWithId(imgpath):
    IDs = []
    IDNum = []
    count = 0
    ImagePaths = []
    for p1 in os.listdir(imgpath):
        count += 1

        for f in os.listdir('dataSet/' + p1):
            if f == 'Thumbs.db':
                os.remove(os.path.join(imgpth,p1,f))
                continue
            print(f)
            IDs.append(p1)
            IDNum.append(count)
            ImagePaths.append(os.path.join(imgpath,p1,f))
    faces = []

    for imagepath in ImagePaths:
        count = 0
        faceImg = Image.open(imagepath).convert('L')
        faceNp = np.array(faceImg,'uint8')
        faces.append(faceNp)
        cv2.imshow('training', faceNp)
        cv2.waitKey(10)

    return IDs, faces, np.array(IDNum)


Ids, faces, IdNum = getImagesWithId(imgpth)
fout.write(str(Ids))
fout.write(str(IdNum))
recog.train(faces, IdNum)
print(len(Ids))
print(len(faces))
recog.write('Recognizer\\trainingData.smfdb')
cv2.destroyAllWindows()
