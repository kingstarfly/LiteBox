# -*- coding: utf-8 -*-
"""pipeline.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Jq7d32D8zHeUQb0G-pzi0f77sOR-ocrj

# Data Augmentation
"""

# Commented out IPython magic to ensure Python compatibility.
## Imports necessary utils and dependencies
from __future__ import absolute_import, division, print_function, unicode_literals

try:
  # The %tensorflow_version magic only works in colab.
#   %tensorflow_version 2.x
except Exception:
  pass
import tensorflow as tf

import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
from google.colab import files
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

"""## Setup Input Pipeline"""

## Creates datagen objects for training and validation
def augs():
  train_datagen=ImageDataGenerator(rescale=1./255, 
                                   height_shift_range=10,
                                   width_shift_range=10,
                                   rotation_range=90,
                                   horizontal_flip=True,
                                   vertical_flip=True,
                                   brightness_range=[0.5, 2.5])

  valid_datagen=ImageDataGenerator(rescale=1./255)

  ## Augments the downloaded data 
  train_generator=train_datagen.flow_from_directory(directory="dishes/train",
                                                   target_size=(224,224),
                                                   color_mode="rgb",
                                                   batch_size=16,
                                                   class_mode="categorical",
                                                   shuffle=True, seed=42)

  valid_generator = valid_datagen.flow_from_directory(directory="dishes/valid",
                                                      target_size=(224, 224),
                                                      color_mode="rgb",
                                                      batch_size=8,
                                                      class_mode="categorical",
                                                      shuffle=True, seed=42)
  
  ## Save the labels in a file which will be downloaded later.
  labels = '\n'.join(sorted(train_generator.class_indices.keys()))

  with open('labels.txt', 'w') as f:
    f.write(labels)
    
  return train_generator, valid_generator

## Plots the learning curves for both training and validation 
def learning_curves(history):
  acc = history.history['accuracy']
  val_acc = history.history['val_accuracy']

  loss = history.history['loss']
  val_loss = history.history['val_loss']

  plt.figure(figsize=(8, 8))
  plt.subplot(2, 1, 1)
  plt.plot(acc, label='Training Accuracy')
  plt.plot(val_acc, label='Validation Accuracy')
  plt.legend(loc='lower right')
  plt.ylabel('Accuracy')
  plt.ylim([min(plt.ylim()),1])
  plt.title('Training and Validation Accuracy')

  plt.subplot(2, 1, 2)
  plt.plot(loss, label='Training Loss')
  plt.plot(val_loss, label='Validation Loss')
  plt.legend(loc='upper right')
  plt.ylabel('Cross Entropy')
  plt.ylim([0,1.0])
  plt.title('Training and Validation Loss')
  plt.xlabel('epoch')
  plt.show()

## Create the base model from the pre-trained model MobileNet V2
def train():
  IMAGE_SIZE = 224
  IMG_SHAPE = (IMAGE_SIZE, IMAGE_SIZE, 3)
  
  train_generator, valid_generator = augs()

  base_model = tf.keras.applications.MobileNetV2(input_shape=IMG_SHAPE,
                                                include_top=False, 
                                                weights='imagenet')
  base_model.trainable = True
  for layer in base_model.layers[:1200]:
    layer.trainable=False
  
  ## Adds additional layers on top of the pre-trained model for fine-tuning 
  model = tf.keras.Sequential([
  base_model,
  tf.keras.layers.Conv2D(32, 3, activation='relu'),
  tf.keras.layers.Dropout(0.3),
  tf.keras.layers.GlobalAveragePooling2D(),
  tf.keras.layers.Dense(20, activation='relu'),
  tf.keras.layers.Dense(2, activation='sigmoid')
  ])
  
  model.compile(optimizer=tf.keras.optimizers.Adam(0.0005), 
              loss='binary_crossentropy', 
              metrics=['accuracy'])
  
  epochs = 5

  history = model.fit_generator(train_generator, 
                                epochs=epochs, 
                                validation_data=valid_generator)
  learning_curves(history)
  
  return model

## Evaluates the model on sample pictures
def preds(image)
  img = cv2.imread(image)
  img_array = cv2.resize(img, (224, 224))
  new_img = np.reshape(img_array, [1, 224, 224, 3])
  new_img = tf.cast(new_img, tf.float32)

  pred = model.predict(new_img)
  return pred

## Saved the model using tf.saved_model.save and then convert the saved model to a tf lite compatible format.
def convert_tflite(model):
  saved_model_dir = 'save/fine_tuning'
  tf.saved_model.save(model, saved_model_dir)

  converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
  tflite_model = converter.convert()

  with open('model.tflite', 'wb') as f:
    f.write(tflite_model)

## Downloads the tflite file and labels file for input into the Android app
if __name__ == '__main__':
  convert_tflite(train())
  files.download('model.tflite')
  files.download('labels.txt')