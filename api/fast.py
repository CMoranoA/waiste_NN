from fastapi import FastAPI
from tensorflow.keras.utils import image_dataset_from_directory
import tensorflow as tf
from tensorflow.keras import models
from waiste.params import IMAGE_WIDTH, IMAGE_HEIGHT, BATCH_SIZE, IMAGE_CHANNELS, CATEGORIES, PATH_TO_LOCAL_MODEL, CATEGORIES_LIST
from waiste.preprocessor import build_data_arrays, cast_image_size
import numpy as np

import pytz


app = FastAPI()

@app.get("/")
def index():
    return {"greeting": "Hello world"}


@app.get("/predict")
def predict():
    filepath = "/Users/cristobalmorano/Desktop/test_asd/lata.jpeg"
    
    image = tf.keras.utils.load_img(
        filepath, grayscale=False, color_mode='rgb', target_size=(128,128),
        interpolation='bilinear')

    image_arr = np.array(image)

    image_norm = cast_image_size(image_arr)

    image_norm = np.array(image_norm)

    image_final = image_norm.reshape(-1, 128, 128, 3)
    
    model = models.load_model(PATH_TO_LOCAL_MODEL, compile = True)

    predict1 = model.predict(image_final)
    
    print(predict1)
    return CATEGORIES_LIST[np.argmax(predict1)]
