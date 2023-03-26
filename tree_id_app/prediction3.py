import os
import numpy as np
import tensorflow as tf
from keras.utils import image_dataset_from_directory

class_names_cd = ['coniferous', 'deciduous']
class_names_c = ['Pinus Pinaster', 'Pinus Pinea']
class_names_d = ['Eucalyptus', 'Quercus Rotundifolia', 'Quercus Suber']

model_cd = tf.keras.models.load_model('tf_model/model_CorD')
model_c = tf.keras.models.load_model('tf_model/model_coniferous')
model_d = tf.keras.models.load_model('tf_model/model_deciduous')

def normalize_pixels(image,label):
    image = tf.cast(image/255. ,tf.float32)
    return image,label

def predicting(imgpath):
    
    path_testdata = os.path.dirname(os.path.dirname(imgpath))

    test_dataset = image_dataset_from_directory(
        path_testdata,
        color_mode='rgb',
        image_size=(150, 150)
    )
    test_dataset = test_dataset.map(normalize_pixels)

    prediction_cd = model_cd.predict(test_dataset)
    print(prediction_cd) #[[0.02200979 0.97799015]]

    if prediction_cd[0][0] > 0.5:
        prediction_c = model_c.predict(test_dataset)

        indices = np.argsort(prediction_c)[::1]
        #prediction name:
        pred = class_names_c[indices[0][-1]]
        #prediction strenght:
        acc = round(prediction_c[0][indices[0][-1]]*prediction_cd[0][0]*100,)
        pred2 = class_names_c[indices[0][-2]]
        acc2 = round(prediction_c[0][indices[0][-2]]*prediction_cd[0][0]*100,)
        pred3 = class_names_c[indices[0][-2]]
        acc3 = 0
    
    else:
        prediction_d = model_d.predict(test_dataset)
        print(prediction_d)

        indices = np.argsort(prediction_d)[::1]
        #prediction name:
        pred = class_names_d[indices[0][-1]]
        #prediction strenght:
        acc = round(prediction_d[0][indices[0][-1]]*prediction_cd[0][1]*100,)
        pred2 = class_names_d[indices[0][-2]]
        acc2 = round(prediction_d[0][indices[0][-2]]*prediction_cd[0][1]*100,)
        pred3 = class_names_d[indices[0][-3]]
        acc3 = round(prediction_d[0][indices[0][-3]]*prediction_cd[0][1]*100,)

    return (pred, acc, pred2, acc2, pred3, acc3)

if __name__ == "__main__":
    imgpathtest = "C:\\Users\\mycro\\Verwaltung\\all_things_tec\\Weeks\\Week9\\Project\\tree_id_app\\tree_id_app\\static\\test_inputs\\class\\what_kind_of_tree_is_this5.jpg"
    pred = predicting(imgpathtest)
    print(pred)