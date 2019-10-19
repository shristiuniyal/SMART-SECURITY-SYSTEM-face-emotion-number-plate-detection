#!/usr/bin/env python
# coding: utf-8

# In[62]:


import numpy as np
import cv2
import pytesseract
import tesserocr


# In[67]:


tesseract_location="C:\\Program Files\\Tesseract-OCR\\tessdata"
pytesseract.pytesseract.tesseract_cmd=tesseract_location
plates=cv2.CascadeClassifier('F:\\ImageProcessing\\plates.xml')


# In[68]:


flag=0
cap=cv2.VideoCapture("F:\\ImageProcessing\\platerec.mp4")
while(True):
    ret,frame=cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    plate=plates.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in plate:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),10)
        flag=flag+1
        pic=frame[y:y+h,x:x+w]
        flag=str(flag)
        cv2.imwrite("F:\\ImageProcessing\\no_plates\\"+flag+".jpg",pic)
        flag=int(flag)
    cv2.imshow('webcam',frame)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
cap.release()


# In[ ]:




