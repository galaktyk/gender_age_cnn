import numpy as np
import cv2
import os
from tensorflow.contrib.keras import backend as K
from tensorflow.keras.models import load_model
import sys
import tensorflow as tf
tf.test.gpu_device_name()
import time

model = load_model('my_model256.h5')
gender_dict = ['male : ','female : ']
age_dict = ['(0-2)','(4-6)','(8-12)','(15-20)','(25-32)','(38-43)','(48-53)','(60-100)']

video_capture = cv2.VideoCapture(0)      
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
t=[time.time()]

while True:

    ret, frame = video_capture.read()
    frame = cv2.flip(frame,1)

    ## face_detect --------------------------------
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face = face_detector.detectMultiScale(gray,scaleFactor = 1.2, minNeighbors = 5 \
        ,minSize = (200,200),flags = cv2.CASCADE_SCALE_IMAGE)#(x,y,w,h)
    if len(face) != 0:    
        (x,y,w,h) = face[0]       

        ## feed CNN --------------------------------
        xde = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)    
        xde = xde[y:(y+h),x:(x+w)]
        xde = cv2.resize(frame, (256, 256)) 
        xde = xde / 255.
        xde = np.expand_dims(xde, axis=0)
        genderp,agep = model.predict(xde)


        ## Show --------------------------------------
        text = gender_dict[genderp.argmax()]+age_dict[agep.argmax()]

        t.append(time.time())
        fps = 1/(t[1]-t[0])
        t.pop(0)


        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0), 3)      
        cv2.putText(frame, text,(5,30),cv2.FONT_HERSHEY_SIMPLEX, 5e-3 * 200, (0,255,0),2)
        cv2.putText(frame, 'FPS : {:.2f}'.format(fps),(5,470),cv2.FONT_HERSHEY_SIMPLEX, 5e-3 * 100, (0,0,255),2)

        

    cv2.imshow('', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break












