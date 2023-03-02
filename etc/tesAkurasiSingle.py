import cv2
import os
from simple_facerec import SimpleFacerec
import pandas as pd
import datetime as dt
import mysql.connector

# akses database
'''
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="eksdee2506",
    database="test"
)
mycursor = mydb.cursor()
'''
unknownID = 1
dirTrain = 'WajahDatabase'


# encoding wajah
sfr = SimpleFacerec()
sfr.load_encoding_images("WajahDatabase/")

# pilih camera
cap = cv2.VideoCapture(0)
frameCounter = 0
counterWajah = 0
EpoCounter = 0
RickoCounter = 0

while True:
    ret,  frame = cap.read()

    # deteksi wajah
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x1, y2, x2 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        cv2.putText(
            frame, 
            name, 
            (x2, y1-10),
            cv2.FONT_HERSHEY_DUPLEX, 
            1, 
            (0, 255, 255), 
            2
            )
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 0), 4)
        # tambahan untuk capture unknown
        namaFile = str(name)+str(unknownID)+'.jpg'
        '''
        if name == 'Revelino':
            EpoCounter = EpoCounter + 1
        if name == 'Rais':
            RickoCounter = RickoCounter + 1
        if face_names != []:
            counterWajah = counterWajah + 1
        '''
    cv2. imshow("Frame", frame)
    '''
    # rekam data unknown
    if name == "Unknown":
        frameCap = cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 0), 4)
        cv2.imwrite(dirTrain+'/'+namaFile, frameCap)
        unknownID += 1
    else:
        # input data ke database
        mycursor.execute(
            "UPDATE History SET absen = %s, timestamp = CURRENT_TIMESTAMP WHERE name = %s", (True, name))
        mydb.commit()
    '''
    frameCounter = frameCounter + 1

    # tutup aplikasi
    key = cv2.waitKey(1)
    if key == 27:
        break

# mydb.close()
cap.release()
print("Dalam jumlah frame = %s terdeteksi %s wajah dan %s dari wajah terdeteksi Revelino serta %s wajah Rais" %
      (frameCounter, counterWajah, EpoCounter, RickoCounter))
cv2.destroyAllWindows()
