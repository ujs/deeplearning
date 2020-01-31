#Word level one hot encoding

import numpy as np
import string

samples =  ['the cat went for a walk', 'the dog ate my burger']



max_len = 10

def tokenization(samples):
    token_dict = {}
    for sample in samples:
        for word, key in enumerate(sample.split()):
            if key not in token_dict:
            token_dict[key] = word
    dimensionality = len(token_dict)

    return token_dict, dimensionality





def one_hot_encoding(samples, max_len):

    token_dict, dimensionality = tokenization(samples)
    encoded = np.zeros((len(samples),max_len, dimensionality))

    for sample in samples:
        for token in


    return encoded
