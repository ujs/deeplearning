

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


# Normalizing data - n samples(rows), m attributes(columns)

mean = data[:].mean(axis = 0) #columnwise mean in matrix form
data -= data- mean
std = data[:].std(axis = 0)
data /= std
