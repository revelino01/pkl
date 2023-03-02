import cv2

cam=cv2.VideoCapture(0)
while True:
    retV, frame = cam.read()
    abuabu=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Webcamku',frame)
    cv2.imshow('webcamku',abuabu)
    k = cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()