import cv2
cap = cv2.VideoCapture(0)
 
while cap.isOpened():
 ret, img = cap.read()
 
#apply same face detection procedures
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
 
for (x,y,w,h) in faces:
 cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

 
cap.release()
cv2.destroyAllWindows()
