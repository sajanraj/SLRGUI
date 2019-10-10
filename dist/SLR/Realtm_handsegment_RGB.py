
import os,cv2
import numpy as np
from keras import backend as K
K.set_image_dim_ordering('tf')

var=os.getcwd()
var2 = var+'\\test_sample\\0\\sample.jpeg'
print (var2)
#contor
def bbox(image,count,disp,model,value):
    #disp
    import cv2
    img=image
    import numpy as np
    import cv2
    #CLAHE (Contrast Limited Adaptive Histogram Equalization)
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    # -----Splitting the LAB image to different channels------
    l, a, b = cv2.split(lab)
    # -----Applying CLAHE to L-channel--------
    clahe = cv2.createCLAHE(clipLimit=5.0, tileGridSize=(3, 3))
    cl = clahe.apply(l)
    limg = cv2.merge((cl, a, b))
    limg = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    #cv2.imshow('CLACHE',limg)
    #end CLACHE
    gray = cv2.cvtColor(limg, cv2.COLOR_BGR2HSV)
    #cv2.imshow('clache',gray)
    blur = cv2.bilateralFilter(gray,9, 100,100)
    gaus = cv2.GaussianBlur(blur, (5, 5), 1)
    median = cv2.medianBlur(gaus, 3)
    #cv2.imshow('median',median)
    COLOR_MIN = np.array([value[0],value[1],value[2]], np.uint8)
    COLOR_MAX = np.array([value[3],value[4], value[5]], np.uint8)
    blur = cv2.inRange(median, COLOR_MIN, COLOR_MAX)
    #ret, thresh1 = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    #ret, thresh1 = cv2.threshold(blur, 127, 255,0)
    rnt,contours, hierarchy = cv2.findContours(blur,cv2.RETR_TREE,cv2.CHAIN_APPROX_TC89_KCOS)
    # Find the index of the largest contour
    areas = [cv2.contourArea(c) for c in contours]
    #print(contours)
    #print(areas)
    if (areas!=[]):
        max_index = np.argmax(areas)
        cnt=contours[max_index]
        x, y, w, h = cv2.boundingRect(cnt)
        #croped image (ROI) 1st box
        #fit box
        #if h>200:
        #    h=200
        #w = int((3*h)/4)
        #save = img[y:y+200,x:x+200]
        save1 = img[50:350, 50:350]
        cv2.imshow('crop',save1)
        #predcit cnn using dataset
        if (count==5 or count==10 or count==15 or count==20 or count==25 or count==30):
            save = predt(save1,model)
            disp1=save
        else:
            disp1 = str(disp[0])
        cv2.putText(img, str(disp1), (50, 50), cv2.FONT_HERSHEY_SIMPLEX,1, 255,2)
        frame = cv2.rectangle(img, (50, 50), (50 + 300, 50 + 300), (0, 255, 0), 2)
        # second bounding box finding
        areas2 = sorted(areas)
        lent = len(areas2)
        area2 = areas.index(areas2[lent-2])
        cnt = contours[area2]
        x, y, w, h = cv2.boundingRect(cnt)
        if h > 200:
            h = 200
        #w = int((3 * h) / 4)
        # croped image (ROI) 2nd box
        save2 = img[50:350, 50:350]
        #save2 = img[y:y + 300, x:x + 300]
        # predcit cnn using dataset
        if (count==5|count==10|count==15|count==20|count==25|count==30):
           save2 = predt(save2,model)
           disp2 = save2
        else:
            print(disp)
            disp2=str(disp[1])
        #cv2.putText(img, str(disp2), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)
        #frame = cv2.rectangle(img, (x, y), (x + 300, y + 300), (0, 255, 0), 2)
        disp=[disp1 ,disp2]
    else:
        frame=rnt



    return frame, rnt,disp

def rec(frame):
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    frame=cv2.imshow("Show", frame)
    return frame

def predt(save,model):
    #model = load_model('E:\\backup\project-sajan\keras_cnn_sample_test0-9\ISL_test_1_model\\isl_model_128.h5')
    #frame = cv2.resize(save, (256, 256))

    from keras.preprocessing import image
    cv2.imwrite('temp.jpg',save)

    test_image = image.load_img('temp.jpg', target_size=(256, 256))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    # result = classifier.predict(test_image)
    # frame = frame.transpose(( 2, 0, 1))

    Y_pred = model.predict_classes(test_image)
    classary = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    print(Y_pred)
    return classary[Y_pred[0]]