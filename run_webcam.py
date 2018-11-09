from keras.models import load_model
import cv2
import numpy as np
import time

model = load_model('my_model256.h5')
gender_dict = ['male : ','female : ']
age_dict = ['(0-2)','(4-6)','(8-12)','(15-20)','(25-32)','(38-43)','(48-53)','(60-100)']

video_capture = cv2.VideoCapture(0)      

t=[time.time()]

while True:

    


    ret, frame = video_capture.read()
    frame = cv2.flip(frame,1)      
    x = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    x = x[75:480-75,155:640-155]
    x = cv2.resize(frame, (256, 256)) 
    x = x / 255.
    x = np.expand_dims(x, axis=0)

    genderp,agep = model.predict(x)

    text = gender_dict[genderp.argmax()]+age_dict[agep.argmax()]

    t.append(time.time())
    fps = 1/(t[1]-t[0])
    t.pop(0)


    cv2.rectangle(frame, (155, 75), (640-155,480-75),(0,255,0), 3)      
    cv2.putText(frame, text,(5,30),cv2.FONT_HERSHEY_SIMPLEX, 5e-3 * 200, (0,255,0),2)
    cv2.putText(frame, 'FPS : {:.2f}'.format(fps),(5,470),cv2.FONT_HERSHEY_SIMPLEX, 5e-3 * 100, (0,0,255),2)

    

    cv2.imshow('', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break












