

import numpy as np
import string

#Word level one hot encoding

samples =  ['the cat is on the run went for a walk', 'the dog ate my burger']

max_len = 25

def tokenization(samples):
    token_dict = {}
    for sample in samples:
        for word in sample.split():
            if word not in token_dict:
                token_dict[word] = len(token_dict)
    dimensionality = len(token_dict)

    return token_dict, dimensionality





def one_hot_encoding(samples, max_len):

    token_dict, dimensionality = tokenization(samples)
    encoded = np.zeros((len(samples),max_len, dimensionality))

    for i,sample in enumerate(samples):
        for j, token in enumerate(sample.split()):
            index = token_dict[token]

            encoded[i][j][index] = 1

    return encoded

#Word embedding
from keras.layers import Embedding
embedding_layer = Embedding(1000,64)

from keras.datasets import imdb
from keras import preprocessing

max_features = 1000
max_len = 20

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)

x_train = preprocessing.sequence.pad_sequences(x_train, maxlen = max_len)
x_test = preprocessing.sequence.pad_sequences(x_test, maxlen = max_len)

#IMDB example- extracting labels and reviews into lists

import os

root_path = ....
train_dir = os.path.join(root_path, 'train')
labels, texts = [],[]

for type in ['neg','pos']:
    dir_name= os.path.join(train_dir,type)
    for fname in os.listdir(dir_name):
        if fname[-4:] = 'txt':
            f = open(os.join.path(dir_name,fname))
            text.append(f.read())
            f.close()
            if type == 'neg':
                labels.append(0)
            else: labels.append(1)

#Using pretrained embeddings- example Glove

#parsing the data in the form of a dictionary (key is word, value is an array with vector components)
glove_dir = os.join.path (root_path, 'glove.6B')


f= open(os.join.path(glove_dir, 'glove.6B.100d.txt'))
embeddings = {}

for line in f:
    values = line.split()
    word = values[0]
    vector_values = np.asarray(vallues[1:], dtype = 'float32')
    embeddings[word] = vector_values

f.close()
