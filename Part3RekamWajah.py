import cv2 , os
import numpy as np
import face_recognition

cam=cv2.VideoCapture(0)
cam.set(3, 640) #mengubah lebar camera
cam.set(4, 480) #mengubah tinggi camera
WajahDir = 'WajahDatabase'
faceDetector = cv2.CascadeClassifier('DeteksiWajah.xml')
eyeDetector = cv2.CascadeClassifier('DeteksiMata.xml')
faceID = input("Masukkan Nama, lalu tekan enter: ")
print("Hadapkan muka ke kamera dan tunggu proses selesai")
ambilData = 1

while True:
    retV, frame = cam.read()
    abuAbu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces  = faceDetector.detectMultiScale(abuAbu, 1.3, 5) #frame,scaleFactor,minMaxBurst
    for(x, y, w, h) in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
        namaFile = 'wajah.'+str(faceID)+'.'+str(ambilData)+'.jpg'
        cv2.imwrite(WajahDir+'/'+namaFile, frame) ##hanya buat testing
        ambilData += 1
        roiAbuAbu = abuAbu[y:y+h,x:x+w]
        roiWarna = frame[y:y+h,x:x+w]
        eyes = eyeDetector.detectMultiScale(roiAbuAbu)
        for (xe,ye,we,he) in eyes:
            cv2.rectangle(roiWarna,(xe,ye),(xe+we,ye+he),(0,0,255),1)

    cv2.imshow('Webcamku', frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord ('q'):
        break
    elif ambilData>10:
        break
print ("Pengambilan data selesai")
cam.release()
cv2.destroyAllWindows()

