from tensorflow.keras.models import load_model
import cv2

import numpy as np
import cv2
import os
from tensorflow.contrib.keras import backend as K
from tensorflow.keras.models import load_model
import sys
import tensorflow as tf
tf.test.gpu_device_name()
import time

model = load_model('my_model256age.h5')
input_size = 256
gender_dict = ['male : ','female : ']
age_dict = ['(0-2)','(4-6)','(8-12)','(15-20)','(25-32)','(38-43)','(48-53)','(60-100)']

video_capture = cv2.VideoCapture(0)      
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
t=[time.time()+1]

while True:


    ret, frame = video_capture.read()
    frame = cv2.flip(frame,1)


    ## face_detect --------------------------------
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face = face_detector.detectMultiScale(gray,scaleFactor = 1.1, minNeighbors = 5 ,minSize = (200,200),flags = cv2.CASCADE_SCALE_IMAGE)#(x,y,w,h)
    if len(face) != 0:    
        (x1,y1,w,h) = face[0]
        
        x1 = int(x1-w*0.2)
        w = int(w*1.4)
        y1 = int(y1-h*0.2)
        h = int(h*1.4) 


        ## feed CNN --------------------------------
        xde = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)    
        xde = xde[y1:(y1+h),x1:(x1+w)]
        xde = cv2.resize(frame, (input_size, input_size)) 
        xde = xde / 255.
        xde = np.expand_dims(xde, axis=0)
        genderp,agep= model.predict(xde)


        ## Show -------------------------------------- 
        text1 = gender_dict[genderp.argmax()]+'{:.2f}'.format(np.max(genderp))
        text2 = age_dict[agep.argmax()]+'{:.2f}'.format(np.max(agep))
        t.append(time.time())
        fps = 1/(t[1]-t[0])
        t.pop(0)

        cv2.rectangle(frame, (x1,y1),(x1+w,y1+h),(0,255,0), 3)     
        cv2.putText(frame, text1,(5,30),cv2.FONT_HERSHEY_SIMPLEX, 5e-3 * 200, (0,255,0),2)
        cv2.putText(frame, text2,(5,100),cv2.FONT_HERSHEY_SIMPLEX, 5e-3 * 200, (0,255,0),2)
        cv2.putText(frame, 'FPS : {:.2f}'.format(fps),(5,470),cv2.FONT_HERSHEY_SIMPLEX, 5e-3 * 100, (0,0,255),2)
        
            

    cv2.imshow('', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  











