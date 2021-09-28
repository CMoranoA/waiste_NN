from waiste.params import IMAGE_CHANNELS, IMAGE_HEIGHT
import numpy as np

from waiste.data import get_data
from waiste.params import IMAGE_WIDTH, IMAGE_HEIGHT, IMAGE_CHANNELS, IMAGE_SIZE, CATEGORIES
from waiste.preprocessor import build_data_arrays, cast_image_size


class Trainer():
    def __init__(self):
        self.x_train = None
        self.y_train = None

    def train(self):
        # Get data
        data = get_data()
        # Take full batches
        data = data.take(700)
        # Preprocessing
        data_images, data_labels = build_data_arrays(data)
        data_images_casted = [cast_image_size(image) for image in data_images]
        data_images_casted = np.array(data_images_casted)
        data_labels = np.array(data_labels)
        data_images_casted = data_images_casted.reshape(
            -1, IMAGE_WIDTH, IMAGE_HEIGHT, IMAGE_CHANNELS)
        data_labels = data_labels.reshape(-1, CATEGORIES)
        
        # Split the dataset
        self.x_train, self.y_train, self.x_valid, self.y_valid = split_data(
            np.array(image_paths), np.array(labels))

        model = self.build_model()
        model.fit(train_dataset,
                  validation_data=validation_dataset,
                  epochs=EPOCHS,
                  callbacks=[EARLY_STOPPING],
                  batch_size=TRAINING_BATCH_SIZE)
        self.model = model
        models.save_model(model, PATH_TO_LOCAL_MODEL)
        return model

    def build_model(self):
        return model


if __name__ == '__main__':
    trainer = Trainer()
    model = trainer.train()
