import cv2
import numpy as np

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner/trainner.yml')
face_Cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");




cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=face_Cascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        print("id ", Id)
        #print("conf ", conf)
        if(Id==12):
            Id="Steve Jobs"
        elif(Id==15):
            Id="Bill Gates"
        else:
            Id="Unknown"
        cv2.putText(im,str(Id), (x,y+h),font,0.55,(255,255,255),1)
    cv2.imshow('im',im)
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()



