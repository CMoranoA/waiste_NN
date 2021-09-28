from tensorflow.keras.utils import image_dataset_from_directory

def get_data():
    filepath = "../waiste/data"
    data = image_dataset_from_directory(filepath,
                                        labels='inferred',
                                        label_mode='categorical',
                                        class_names=None,
                                        color_mode='rgb',
                                        batch_size=32,
                                        image_size=(76, 76),
                                        shuffle=True,
                                        seed=None,
                                        validation_split=None,
                                        subset=None,
                                        interpolation='bilinear',
                                        follow_links=False,
                                        crop_to_aspect_ratio=False)
    return data
