import cv2 , os
import numpy as np
from PIL import Image

WajahDir = 'WajahDatabase'
LatihDir = 'LatihWajah'

def getImageLabel(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    faceSamples = []
    faceIDs = []
    for imagePath in imagePaths:
        PILImg = Image.open(imagePath).convert('L') #convert gambar menjadi grayscale
        imgNum = np.array(PILImg, 'vint8')
        faceID = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = faceDetector.datectMultiScale(imgNum)
        for(x, y, w, h) in faces:
            faceSamples.append(imgNum[y:y+h,x:x+w])
            faceIDs.append(faceID)
        return faceSamples,faceIDs

faceRecognizer = cv2.face.LBPHFaceRecognizer_create()
faceDetector = cv2.CascadeClassifier('DeteksiWajah.xml')

print("Mesin sedang melakukan training dara wajah. Tunggu dalam beberapa saat")
faces,IDs = getImageLabel(WajahDir)
faceRecognizer.train(faces,np.array(IDs))

#save
faceRecognizer.write(LatihDir+'/trainer.xml')
print ('sebanyak {0} data wajah telah digunakan untuk training mesin',format(len(np.unique(IDs))))

