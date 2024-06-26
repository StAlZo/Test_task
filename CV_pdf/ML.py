import cv2
from PIL.ImageTransform import AffineTransform
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# def make_background():
#     image = ' '
#     file_without_extension = image.split('.')[0]
#     image = cv2.imread(image, cv2.IMREAD_UNCHANGED)
#     trans_mask = image[:, :, 3] == 0
#     image[trans_mask] = [255, 255, 255, 255]
#     new_img = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
#     cv2.imwrite(file_without_extension + '.jpeg', new_img)
#
#
# def shift():
#     image = ''
#     img = cv2.imread(image)
#     file_without_extension = image.split('.')[0]
#     arr_translation = [[15, -15], [-15, 15], [-15, -15],
#                        [15, 15]]
#     arr_caption = ['15-15', '-1515', '-15-15', '1515']
#     for i in range(4):
#         transform = AffineTransform(
#             translation=tuple(arr_translation[i]))
#         warp_image = warp(img, transform, mode="wrap")
#         img_convert = cv2.convertScaleAbs(warp_image,
#                                           alpha=(255.0))
#         cv2.imwrite(file_without_extension +
#                     arr_caption[i] + '.jpeg', img_convert)


import tensorflow as tf
ImageDataGenerator = tf.keras.preprocessing.image.ImageDataGenerator
TRAINING_DIR = "/home/stas/PycharmProjects/Test_task/Cyrillic"
train_datagen = ImageDataGenerator(rescale=1.0 / 255.)
train_generator = train_datagen.flow_from_directory(TRAINING_DIR,
                              batch_size=40,
                              class_mode='binary',
                              target_size=(278,278))

VALIDATION_DIR = "/home/stas/PycharmProjects/Test_task/Cyrillic"
validation_datagen = ImageDataGenerator(rescale=1.0 / 255.)
validation_generator = validation_datagen.flow_from_directory(VALIDATION_DIR,
                                      batch_size=40,
                                      class_mode='binary',
                                      target_size=(278,278))

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(16, (3, 3), activation='relu',
                           input_shape=(278,278, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(33, activation='softmax')
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()
history = model.fit_generator(train_generator,
                               epochs=2,
                               verbose=1,
                               validation_data=validation_generator)

model.save('model.h5')