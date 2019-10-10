def slrlive():
    import os, cv2
    import numpy as np
    from keras import backend as K
    K.set_image_dim_ordering('tf')
    from keras.models import load_model
    from Realtm_handsegment_RGB import bbox, rec
    direc = os.getcwd()

    model = load_model('Model_SLR_try4.h5')
    weight = model.load_weights('Model_SLR_weight_try4.h5')

    disp = [0, 0]
    # model = load_model('isl_model_128.h5')
    num_channel = 3
    # Create a VideoCapture object
    cap = cv2.VideoCapture(0)
    value = [0, 0, 0, 255, 255, 255]
    # Check if camera opened successfully
    if (cap.isOpened() == False):
        print("Unable to read camera feed")

    # Default resolutions of the frame are obtained.The default resolutions are system dependent.
    # We convert the resolutions from float to integer.
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    # Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
    out = cv2.VideoWriter('project_record1.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10,
                          (frame_width, frame_height))
    count = 0
    panel = np.zeros([100, 700], np.uint8)
    while (True):
        ret, frame = cap.read()
        rnt = []
        if ret == True:
            count = count + 1

            def nothing(x):
                pass

            cv2.namedWindow('panel')
            # COLOR_MIN = np.array([120, 20, 70], np.uint8)
            # COLOR_MAX = np.array([200, 100, 160], np.uint8)
            cv2.createTrackbar('L_H', 'panel', 120, 255, nothing)
            cv2.createTrackbar('U_H', 'panel', 255, 255, nothing)
            cv2.createTrackbar('L_S', 'panel', 35, 255, nothing)
            cv2.createTrackbar('U_S', 'panel', 255, 255, nothing)
            cv2.createTrackbar('L_V', 'panel', 30, 255, nothing)
            cv2.createTrackbar('U_V', 'panel', 225, 255, nothing)
            l_h = cv2.getTrackbarPos('L_H', 'panel')
            u_h = cv2.getTrackbarPos('U_H', 'panel')
            l_s = cv2.getTrackbarPos('L_S', 'panel')
            u_s = cv2.getTrackbarPos('U_S', 'panel')
            l_v = cv2.getTrackbarPos('L_V', 'panel')
            u_v = cv2.getTrackbarPos('U_V', 'panel')
            # COLOR_MIN = np.array([l_h,l_s, l_v], np.uint8)
            # COLOR_MAX = np.array([u_h, u_s, u_v], np.uint8)
            value = [l_h, l_s, l_v, u_h, u_s, u_v]

            # globals from the someFile module
            frame, rnt, disp = bbox(frame, count, disp, model, value)
            #    count = 0
            # images = [frame, rnt]

            cv2.imshow('frame', frame)
            #cv2.imshow('image', rnt)
            # Write the frame into the file 'output.avi'
            out.write(frame)
            # cv2.imshow('panel',panel)
            if count == 20:
                count = 0

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Break the loop
        else:
            break

            # When everything done, release the video capture and video write objects
    cap.release()
    out.release()

    # Closes all the frames
    cv2.destroyAllWindows()


def slrtest(path):
    import os, cv2
    import numpy as np
    from keras import backend as K
    K.set_image_dim_ordering('tf')
    from keras.models import load_model
    from keras.preprocessing import image
    model = load_model('Model_SLR_try4.h5')
    weight = model.load_weights('Model_SLR_weight_try4.h5')
    test_image = image.load_img(path, target_size = (256,256))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    #result = classifier.predict(test_image)
    #frame = frame.transpose(( 2, 0, 1))
   
    Y_pred = model.predict_classes(test_image)
    print(Y_pred[0])
    classary = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    return classary[Y_pred[0]]
    # y_pred = np.argmax(Y_pred, axis=1)
    # print(y_pred)
    #while (True):
    #    if cv2.waitKey(1) & 0xFF == ord('q'):
    #        break
