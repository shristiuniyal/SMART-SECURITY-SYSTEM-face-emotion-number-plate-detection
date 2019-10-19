import cv2
import numpy as np
import serial #Serial imported for Serial communication
import time #Required to use delay functions
#ser = serial.Serial('com6', 9600)
#time.sleep(2) #wait for 2 seconds for the communication to get established

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.load("trainner\trainner.yml")
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);


cam = cv2.VideoCapture(0)
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        print(Id)
        
        print(conf)
        if(conf<70):
            if(Id==1):
               # ser.write(str(Id))
                Id="shristi"
            elif(Id==2):
                #ser.write(str(Id))
                Id="shristi"
          
                
        else:
            
            Id="Unknown"
            #ser.write('0')
            cv2.imwrite("unknown/User."+Id +'.'+ ".jpg", gray[y:y+h,x:x+w])
            
        cv2.cv.PutText(cv2.cv.fromarray(im),str(Id), (x,y+h),font, 255)
    cv2.imshow('im',im) 
    if cv2.waitKey(10)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
