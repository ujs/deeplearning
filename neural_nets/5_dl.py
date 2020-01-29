#Naive CNN MNIST DATA

from keras import layers
from keras import models

model = models.Sequential()

model.add(layers.Conv2D(32, (3,3), activation = 'relu', input shape = (28, 28, 1)))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(64,(3,3),activation = 'relu'))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(64,(3,3),activation = 'relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation = 'relu'))
model.add(layers.Dense(10, activation = 'softmax'))

model.summary()

# MNIST data preprocessing

from keras.datasets import MNIST
from keras.utils import to_categorical

(train_images, train_labels) , (test_images, test_labels) = mnist.load_data()

train_images = train_images.reshape((60000,28,28,1))
train_images = train_images.astype(float64)/255

test_images = test_images_images.reshape((10000,28,28,1))
test_images = test_images.astype(float64)/255

train_lables = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

#compiltion
model.compile(optimizer = 'rmsprop', loss = 'categorical_crossentropy', metrics = ['accuracy'])

#fit and evaluation
model.fit(train_images, train_labels, epochs = 5, batch_size = 64)

test_loss, test_accuracy = model.evaluate(test_images, test_labels)



##################################################################################################################################

#Cat and Dog data CNN
 #Data Generators- used to draw random samples without replacements of image data and convert them to tensors

 from keras.preprocessing.image import ImageDataGenerator

 train_datagen = ImageDataGenerator(rescale = 1./255)
 validation_datagen = ImageDataGenerator(rescale = 1./255)

 train_generator = train_datagen.flow_from_directory(train_dir,target_size= (150,150), batch_size = 20, class_mode = 'binary')
 validation_generator = validation_datagen.flow_from_directory(validation_dir, target_size = (150,150), batch_size = 20, class_mode = 'binary')
