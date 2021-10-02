import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

import tensorflow as tf
from tensorflow.keras import Input, models
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import MaxPool2D, Conv2D, Dense, Flatten, Dropout
from tensorflow.keras.callbacks import EarlyStopping

from waiste.data import get_data
from waiste.params import IMAGE_WIDTH, IMAGE_HEIGHT, IMAGE_CHANNELS, NUMBER_OF_BATCHES, PATH_TO_LOCAL_MODEL
from waiste.preprocessor import build_data_arrays, cast_image_size


### TRAINING VARIABLES
TRAINING_BATCH_SIZE = 64
EPOCHS = 500
EARLY_STOPPING_PATIENCE = 25
EARLY_STOPPING = EarlyStopping(monitor="val_loss",
                                         patience=EARLY_STOPPING_PATIENCE,
                                         restore_best_weights=True)


class Trainer():
    def __init__(self):
        self.model = None

    @tf.autograph.experimental.do_not_convert
    def train(self):
        # Get data
        data = get_data()
        # Take full batches
        data = data.take(NUMBER_OF_BATCHES)
        # Preprocessing
        data_images, data_labels = build_data_arrays(data)
        data_images_casted = [cast_image_size(image) for image in data_images]
        data_images_casted = np.array(data_images_casted)
        data_labels = np.array(data_labels)
        data_images_casted = data_images_casted.reshape(
            -1, IMAGE_WIDTH, IMAGE_HEIGHT, IMAGE_CHANNELS)
        data_labels = data_labels.reshape(-1, CATEGORIES)

        # Split the dataset
        train_X, test_X, train_y, test_y = train_test_split(
            data_images_casted,
            data_labels,
            test_size=0.2,
            random_state=42)

        # Train and save model
        model = self.build_model()
        model.fit(train_X, train_y,
                  validation_split=0.3,
                  epochs=EPOCHS,
                  callbacks=[EARLY_STOPPING],
                  batch_size=TRAINING_BATCH_SIZE,
                  verbose=1)
        self.model = model
        model.save(PATH_TO_LOCAL_MODEL)
        # models.save_model(model, PATH_TO_LOCAL_MODEL)
        print(model.evaluate(test_X, test_y))
        return model

    def build_model(self):
        inception_resnet_v2 = tf.keras.applications.inception_resnet_v2.InceptionResNetV2(
            include_top=False,
            weights="imagenet",
            input_tensor=None,
            input_shape=(128, 128, 3),
            pooling=None,
            classifier_activation='softmax')
        inception_resnet_v2.trainable = False

        model = Sequential()
        model.add(Input(shape=(128, 128, 3)))

        model.add(inception_resnet_v2)

        model.add(Conv2D(32, (4, 4), padding='same', activation="relu"))
        model.add(MaxPool2D(pool_size=(4, 4), padding='same'))
        model.add(Dropout(0.4))

        model.add(Dense(30, activation='relu'))

        model.add(Conv2D(16, (3, 3), padding='same', activation="relu"))
        model.add(MaxPool2D(pool_size=(2, 2), padding='same'))
        model.add(Dropout(0.3))

        model.add(Flatten())

        model.add(Dense(50, activation='relu'))
        model.add(Dropout(0.2))
        model.add(Dense(10, activation='softmax'))

        model.compile(loss='categorical_crossentropy',
                      optimizer='adam',
                      metrics=["accuracy"])
        return model


if __name__ == '__main__':
    trainer = Trainer()
    model = trainer.train()
    # plot loss
    plt.figure(figsize=(10, 15))
    plt.subplot(211)
    plt.title('Cross Entropy Loss')
    plt.plot(model.history['loss'], color='blue', label='train')
    plt.plot(model.history['val_loss'], color='orange', label='valid')
    plt.legend()
    # plot accuracy
    plt.subplot(212)
    plt.title('Classification Accuracy')
    plt.plot(model.history['accuracy'], color='blue', label='train')
    plt.plot(model.history['val_accuracy'], color='orange', label='valid')
    plt.legend()
