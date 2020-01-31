#Word level one hot encoding

import numpy as np

X=  'the cat sat on the mat'
encoded = np.zeros((len(X),6))

space_size = 6

dict = {}

for value, key in enumerate(X):
    dict[key] = value

for i in encoded[:]:

    one_hot = dict[i]
    encoded[i][one_hot] = 1
