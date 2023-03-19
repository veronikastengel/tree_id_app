import os
import numpy as np
import tensorflow as tf
from keras.utils import image_dataset_from_directory

class_names = ['Eucalyptus', 'Pinus Pinaster', 'Pinus Pinea', 'Quercus Rotundifolia', 'Quercus Suber']

model = tf.keras.models.load_model('tf_model/keras_model')

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
    predictions = model.predict(test_dataset)

    indices = np.argsort(predictions)[::1]
    #prediction name:
    pred = class_names[indices[0][-1]]
    #prediction strenght:
    acc = round(predictions[0][indices[0][-1]]*100,)
    pred2 = class_names[indices[0][-2]]
    acc2 = round(predictions[0][indices[0][-2]]*100,)
    pred3 = class_names[indices[0][-3]]
    acc3 = round(predictions[0][indices[0][-3]]*100,)

    return (pred, acc, pred2, acc2, pred3, acc3)

if __name__ == "__main__":
    imgpathtest = "C:\\Users\\mycro\\Verwaltung\\all_things_tec\\Weeks\\Week9\\Project\\tree_identifier\\static\\test_inputs\\class\\test.jpg"
    pred = predicting(imgpathtest)
    print(pred)