import os
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
from simple_facerec import SimpleFacerec
import pandas as pd
import datetime as dt
import mysql.connector

# akses database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="eksdee2506",
    database="test"
)

unknownID = 1
mycursor = mydb.cursor()
dirUnk = 'WajahDatabase'

# encoding wajah
sfr = SimpleFacerec()
sfr.load_encoding_images("WajahDatabase/")

# pilih camera
#cap = cv2.VideoCapture(0)
cam = PiCamera()
cam.resolution = (640, 480)
cam.framerate = 32
rawCapture = PiRGBArray(cam, size=(640, 480))

time.sleep(0.1)


for PiCam in cam.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    frame = PiCam.array

    # deteksi wajah dan petunjuk lokasinya
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x1, y2, x2 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        cv2.putText(frame, name, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 0), 4)
        # tambahan untuk capture unknown
        namaFile = str(name)+str(unknownID)+'.jpg'

    # output camera
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # rekam data unknown
    if name == 'Unknown':
        frameCap = cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 0), 4)
        cv2.imwrite(dirUnk+'/'+namaFile, frameCap)
        unknownID += 1
    else:
        # input data ke database
        mycursor.execute(
            "UPDATE History SET absen = %s, timestamp = CURRENT_TIMESTAMP WHERE name = %s", (True, name))
        mydb.commit()

    # tutup aplikasi

    rawCapture.truncate(0)
    if key == 27:
        break

mydb.close()
# cap.release()
cv2.destroyAllWindows()