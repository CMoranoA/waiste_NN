# from tensorflow.keras.utils import image_dataset_from_directory

# from waiste.params import IMAGE_WIDTH, IMAGE_HEIGHT, BATCH_SIZE


# def get_data():
#     filepath = "/Users/cristobalmorano/code/nadiasalmen/waiste/waiste/data"
#     data = image_dataset_from_directory(filepath,
#                                         labels='inferred',
#                                         label_mode='categorical',
#                                         class_names=None,
#                                         color_mode='rgb',
#                                         batch_size=BATCH_SIZE,
#                                         image_size=(IMAGE_WIDTH, IMAGE_HEIGHT),
#                                         shuffle=True,
#                                         seed=None,
#                                         validation_split=None,
#                                         subset=None,
#                                         interpolation='bilinear',
#                                         follow_links=False,
#                                         crop_to_aspect_ratio=False)
#     return data

# def get_categories():
#     data = get_data()
#     categories = data.class_names
#     print(categories)
#     return categories

# if __name__ == '__main__':
#     get_categories()
