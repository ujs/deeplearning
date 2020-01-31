#Word level one hot encoding

import numpy as np
import string

samples =  ['the cat went for a walk', 'the dog ate my burger']



max_len = 10

def tokenization(samples):
    token_dict = {}
    for sample in samples:
        for value, key in enumerate(samples.split(' ')):
            if key not in token_dict:
            token_dict[key] = value
    dimensionality = len(token_dict)

    return token_dict, dimensionality





def one_hot_encoding(samples, dimensionality, max_len):

    encoded = np.zeros((len(samples),max_len, dimensionality))



    dict = {}

    for value, key in enumerate(X):
        dict[key] = value

    for i in encoded[:]:

        one_hot = dict[i]
        encoded[i][one_hot] = 1
    return encoded
