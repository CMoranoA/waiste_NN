from fastapi import FastAPI
import tensorflow as tf
from tensorflow.keras import models
from waiste.params import PATH_TO_LOCAL_MODEL
from waiste.preprocessor import cast_image_size
from waiste.data import get_categories
import numpy as np

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
    
    categories_list = get_categories()
    
    print(predict1)
    return categories_list[np.argmax(predict1)]
