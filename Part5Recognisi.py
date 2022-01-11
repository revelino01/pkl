import cv2, os
import numpy as py

WajahDir = 'WajahDatabase'
LatihDir = 'LatihWajah'
cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)
faceDetector = cv2.CascadeClassifier('DeteksiWajah.xml')
faceRecognizer = cv2.face.LBPHFaceRecognizer_create()

faceRecognizer.read(LatihDir+'/training.xml')
font = cv2.FONT_HERSHEY_SIMPLEX

id = 0
names = ['Tidak Diketahui','Sugiyanto','Nama Lain']

minWidth = 0.1*cam.get(3)
minHeight = 0.1*cam.get(4)

while True:
    retV, frame = cam.read()
    frame = cv2.flip(frame, 1) #flip menjadi vertical
    abuAbu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces  = faceDetector.detectMultiScale(abuAbu, 1.2, 5,minSize=(round(minWidth),round(minHeight)),) #frame,scaleFactor,minMaxBurst
    for(x, y, w, h) in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        id, confidence = faceRecognizer.predict(abuAbu[y:y+h,x:x+w]) #confidence = 0 (cocok sempurna)
        if confidence <= 50:
            nameID = names[id]
            confidenceTxt = " {0}%".fornamt(round(100-confidence))
        else:
            nameID = names[0]
            confidenceTxt = " {0}%".fornamt(round(100-confidence))
        cv2.putText(frame,str(nameID),(x+5,y-5),font,1,(255,255,255),2)
        cv2.putText(frame,str(confidenceTxt),(x+5,y+h-5),font,1,(255,255,0),1)
    cv2.imshow('Recognisi Wajah', frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord ('q'):
        break
print ("EXIT")
cam.release()
cv2.destroyAllWindows()
