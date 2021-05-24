import cv2
import numpy as np
from PIL import Image
from skimage import morphology
import tensorflow as tf
from keras.models import model_from_json
from tensorflow.keras.applications.resnet50 import preprocess_input


def fn_load_json_weight(list_json='model_file.json',
                        list_weight='weight_file.h5'):
    json_file = open("./model/" + list_json, 'r')
    model = json_file.read()
    json_file.close()
    model = model_from_json(model)
    model.load_weights('./model/' + list_weight)
    return model

def bwareaopen(imgBW, areaPixels):
    imgBWcopy = imgBW.copy()
    contours,_ = cv2.findContours(imgBWcopy.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

def predict(upload_image):
    model = fn_load_json_weight()

    img_real = np.array(upload_image)
    img = cv2.cvtColor(img_real, cv2.COLOR_BGR2GRAY)
    # img = np.array(upload_image.convert('L'))
    cell_names = ['hela', 'huh-7', 'MCF-7', 'NCI']

    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

    font = cv2.FONT_HERSHEY_SIMPLEX

    img_size = 200
    ret, img_result1 = cv2.threshold((img * 2), 130, 255, cv2.THRESH_BINARY)

    # img_result1= np.array(img_result1,dtype=np.uint8)
    img_result1[985:, 1262:] = 0
    img_result2 = cv2.adaptiveThreshold(img_result1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 7, 30)

    kernel = np.ones((2, 2), np.uint8)
    result = cv2.dilate(img_result2, kernel, iterations=1)

    img_border = result.copy()
    labels = morphology.label(img_border, background=255)
    labelCount = np.bincount(labels.ravel())
    background = np.argmax(labelCount)
    img_border[labels != background] = 255

    final = bwareaopen(img_border, 500)
    # final= bwareaopen(img_border,500)

    final2 = final.copy()
    final2[final2 == 255] = 1
    img_Nbackground = img * final2

    img_result = []
    img_for_class = img_Nbackground.copy()

    contours, _ = cv2.findContours(img_for_class.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    rects = [cv2.boundingRect(each) for each in contours]

    predictData = np.ndarray((0, 200, 200, 3))
    new_rect = []
    for n, rect in enumerate(rects):
        if rect[2] + rect[3] > 0:
            new_rect.append(rect)

    for rect in new_rect:
        test = img_for_class[rect[1]: rect[1] + rect[3], rect[0]: rect[0] + rect[2]]
        image_expand_1 = np.expand_dims((cv2.resize(test, (img_size, img_size))), axis=2)
        rgb = np.dstack([image_expand_1] * 3)
        image_expand_2 = np.expand_dims(rgb, axis=0)
        predictData = np.concatenate([predictData, image_expand_2], axis=0)

    with tf.device('/device:CPU:0'):
        preprocess = preprocess_input(predictData, data_format=None)
        predicted_num = model.predict(preprocess)


    for i, rect in enumerate(new_rect):
        n = predicted_num[i].argmax()
        #         n=cell_binary[i].index(max(cell_binary[i]))
        #     print(answer,predicted_num)
        #     if(hela_nci_data[i].max()>0.6):
        cv2.putText(img_real, cell_names[n], (rect[0], rect[1]), font, 1, colors[n], 2)
        cv2.rectangle(img_real, (rect[0], rect[1]),
                      (rect[0] + rect[2], rect[1] + rect[3]), colors[n], 1)

    #     plt.figure(figsize=(100,100))

    return (img_real)

