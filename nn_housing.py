#!/usr/bin/env python
# coding: utf-8

# In[2]:


import keras


# In[3]:


from keras.datasets import boston_housing
(train_data, train_targets), (test_data, test_targets) = boston_housing.load_data()


# In[4]:


len(train_data)


# In[5]:


train_data.dtype


# In[6]:


train_data.shape


# In[7]:


train_targets.shape


# In[8]:


train_targets[:5]


# In[9]:


train_targets.ndim


# In[10]:


from keras import models
from keras import layers

def build_model():
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu', input_shape=(train_data.shape[1],)))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
    return model


# In[28]:


import numpy as np
k = 4

num_val_samples = len(train_data)//k
num_epochs = 500
all_scores = []
all_mae_histories = []


# In[29]:


for i in range (k):
    print ('processing fold #', i)
    val_data = train_data[i*num_val_samples:(i+1)*num_val_samples]
    val_targets = train_targets[i*num_val_samples:(i+1)*num_val_samples]
    
    partial_train_data = np.concatenate([train_data[:i * num_val_samples],
                                         train_data[(i + 1) * num_val_samples:]], axis=0)
    
    partial_train_targets = np.concatenate([train_targets[:i * num_val_samples],
                                            train_targets[(i + 1) * num_val_samples:]], axis=0)
                                            
                                            
    model = build_model()
    history = model.fit(partial_train_data, partial_train_targets, validation_data=(val_data, val_targets), epochs = num_epochs, batch_size = 1, verbose = 0  )
    val_mse, val_mae = model.evaluate(val_data, val_targets, verbose=0)
    mae_history = history.history['val_mae']
    all_scores.append(val_mae)
    all_mae_histories.append(mae_history)
    


# In[26]:


history.history.keys()


# In[30]:


import matplotlib.pyplot as plt
plt.plot(range(1, len(average_mae_history) + 1), average_mae_history)
plt.xlabel('Epochs')
plt.ylabel('Validation MAE')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




