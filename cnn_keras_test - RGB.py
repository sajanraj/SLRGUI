import os,cv2
import numpy as np
from keras import backend as K
K.set_image_dim_ordering('th')
from keras.models import load_model
model = load_model('C:\\Users\PROJECT 17\Desktop\Sajan Final RealTime prediction using region of interest\Training\Deep Learning workshop Keras Training\\first_model36symbol.h5')
frame=cv2.imread('C:\\Users\PROJECT 17\Desktop\Sajan Final RealTime prediction using region of interest\Training\Deep Learning workshop Keras Training\data\\validation\\06\\6_0.jpg')
#frame = cv2.resize(frame, (256, 256))
#frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
cv2.imshow('frame', frame)
frame = np.array(frame)
frame = frame.astype('float32')
frame /= 255
#frame = np.expand_dims(frame, axis=4)
#print(frame.shape)
frame1 = np.expand_dims(frame,axis=0)
print(frame1.shape)
#frame = frame.transpose((3, 2, 0, 1))
#print((model.predict(frame)))
Y_pred = model.predict_classes(frame1)
print(Y_pred)
#y_pred = np.argmax(Y_pred, axis=1)
#print(y_pred)
while (True):
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

