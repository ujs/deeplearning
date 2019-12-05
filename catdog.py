#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os, shutil


# In[2]:


# The path to the directory where the original
# dataset was uncompressed
original_dataset_dir = 'algos/datasets/kaggle_original_data'

# The directory where we will
# store our smaller dataset
base_dir = 'algos/datasets/cats_and_dogs_small'
os.mkdir(base_dir)


# In[3]:


# Directories for our training,
# validation and test splits
train_dir = os.path.join(base_dir, 'train')
os.mkdir(train_dir)
validation_dir = os.path.join(base_dir, 'validation')
os.mkdir(validation_dir)
test_dir = os.path.join(base_dir, 'test')
os.mkdir(test_dir)


# In[4]:


# Directory with our training cat pictures
train_cats_dir = os.path.join(train_dir, 'cats')
os.mkdir(train_cats_dir)


# In[5]:


# Directory with our training dog pictures
train_dogs_dir = os.path.join(train_dir, 'dogs')
os.mkdir(train_dogs_dir)


# In[6]:


# Directory with our validation cat pictures
validation_cats_dir = os.path.join(validation_dir, 'cats')
os.mkdir(validation_cats_dir)


# In[7]:


# Directory with our validation dog pictures
validation_dogs_dir = os.path.join(validation_dir, 'dogs')
os.mkdir(validation_dogs_dir)


# In[8]:


# Directory with our validation cat pictures
test_cats_dir = os.path.join(test_dir, 'cats')
os.mkdir(test_cats_dir)


# In[9]:


# Directory with our validation dog pictures
test_dogs_dir = os.path.join(test_dir, 'dogs')
os.mkdir(test_dogs_dir)


# In[10]:


# Copy first 1000 cat images to train_cats_dir
fnames = ['cat.{}.jpg'.format(i) for i in range(1000)]
for fname in fnames:
    src = os.path.join(original_dataset_dir, fname)
    dst = os.path.join(train_cats_dir, fname)
    shutil.copyfile(src, dst)


# In[11]:


# Copy next 500 cat images to validation_cats_dir
fnames = ['cat.{}.jpg'.format(i) for i in range(1000, 1500)]
for fname in fnames:
    src = os.path.join(original_dataset_dir, fname)
    dst = os.path.join(validation_cats_dir, fname)
    shutil.copyfile(src, dst)


# In[12]:


# Copy next 500 cat images to test_cats_dir
fnames = ['cat.{}.jpg'.format(i) for i in range(1500, 2000)]
for fname in fnames:
    src = os.path.join(original_dataset_dir, fname)
    dst = os.path.join(test_cats_dir, fname)
    shutil.copyfile(src, dst)


# In[13]:


# Copy first 1000 dog images to train_dogs_dir
fnames = ['dog.{}.jpg'.format(i) for i in range(1000)]
for fname in fnames:
    src = os.path.join(original_dataset_dir, fname)
    dst = os.path.join(train_dogs_dir, fname)
    shutil.copyfile(src, dst)


# In[14]:


# Copy next 500 dog images to validation_dogs_dir
fnames = ['dog.{}.jpg'.format(i) for i in range(1000, 1500)]
for fname in fnames:
    src = os.path.join(original_dataset_dir, fname)
    dst = os.path.join(validation_dogs_dir, fname)
    shutil.copyfile(src, dst)


# In[15]:


# Copy next 500 dog images to test_dogs_dir
fnames = ['dog.{}.jpg'.format(i) for i in range(1500, 2000)]
for fname in fnames:
    src = os.path.join(original_dataset_dir, fname)
    dst = os.path.join(test_dogs_dir, fname)
    shutil.copyfile(src, dst)


# In[16]:


print('total training cat images:', len(os.listdir(train_cats_dir)))


# In[17]:


print('total training dog images:', len(os.listdir(train_dogs_dir)))


# In[18]:


len(os.listdir(test_dogs_dir))


# In[19]:


print(len(os.listdir(test_cats_dir)))
print(len(os.listdir(validation_dogs_dir)))
print(len(os.listdir(validation_cats_dir)))


# In[20]:


from keras import layers
from keras import models


# In[21]:


model = models.Sequential()

model.add(layers.Conv2D(32,(3,3), activation = 'relu', input_shape = (150,150,3)))
model.add(layers.MaxPooling2D((2,2)))

model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))


# In[22]:



model.summary()


# In[23]:


from keras import optimizers

model.compile(loss='binary_crossentropy',optimizer=optimizers.RMSprop(lr=1e-4), metrics=['acc'])


# In[24]:


from keras.preprocessing.image import ImageDataGenerator


# In[25]:


train_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)


# In[26]:


train_generator = train_datagen.flow_from_directory(train_dir, target_size=(150, 150), batch_size=20, class_mode='binary')


# In[27]:


validation_generator = test_datagen.flow_from_directory(validation_dir, target_size=(150, 150), batch_size=20, class_mode='binary')


# In[28]:


train_generator


# In[29]:


type(train_generator)


# In[30]:


dir(train_generator)


# In[31]:


import sys
from PIL import Image
sys.modules['Image'] = Image 

#model fitting
history = model.fit_generator(train_generator,steps_per_epoch=100,epochs=30,validation_data=validation_generator,
                              validation_steps=50)


# In[45]:


history.history


# In[44]:


history.history.keys()


# In[35]:


model.save('cats_and_dogs_small.h5')


# In[56]:


import matplotlib.pyplot as plt

acc = history.history['acc']
val_acc = history.history['val_acc'] 
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(acc) +1)

plt.plot(epochs, acc, 'bo', label = 'training')
plt.plot(epochs, val_acc, 'b', label = 'validation')

plt.legend()
plt.xlabel('epochs')
plt.ylabel('acc')
plt.title('Training & validation accuracy')
plt.show()


# In[62]:




plt.plot (epochs, loss, 'bo', label = 'training')
plt.plot(epochs, val_loss, 'b', label = 'validation')


plt.legend()
plt.xlabel('epochs')
plt.ylabel('loss')
plt.title('Training & Validation loss')
plt.figure()
    


# In[63]:


model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu',
input_shape=(150, 150, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
model.add(layers.Dropout(0.5))
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy',
optimizer=optimizers.RMSprop(lr=1e-4),
metrics=['acc'])


# In[64]:


train_datagen = ImageDataGenerator(
rescale=1./255,
rotation_range=40,
width_shift_range=0.2,
height_shift_range=0.2,
shear_range=0.2,
zoom_range=0.2,
horizontal_flip=True,)


# In[65]:


test_datagen = ImageDataGenerator(rescale=1./255)


# In[66]:


train_generator = train_datagen.flow_from_directory(
train_dir,
target_size=(150, 150),
batch_size=32,
class_mode='binary')


# In[67]:


validation_generator = test_datagen.flow_from_directory(
validation_dir,
target_size=(150, 150),
batch_size=32,
class_mode='binary')


# In[ ]:


history = model.fit_generator(
train_generator,
steps_per_epoch=100,
epochs=100,
validation_data=validation_generator,
validation_steps=50)


# In[ ]:


model.save('cats_and_dogs_small_2.h5')

acc = history.history['acc']
val_acc = history.history['val_acc'] 
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(acc) +1)

plt.plot(epochs, acc, 'bo', label = 'training')
plt.plot(epochs, val_acc, 'b', label = 'validation')

plt.legend()
plt.xlabel('epochs')
plt.ylabel('acc')
plt.title('Training & validation accuracy')
plt.show()


# In[ ]:


plt.plot(epochs, loss, 'bo', label = 'training')
plt.plot(epochs, val_loss, 'b', label = 'validation')

plt.legend()
plt.xlabel('epochs')
plt.ylabel('loss')
plt.title('Training & validation loss')
plt.show()

