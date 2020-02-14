from keras import Input, layers
input_tensor = Input(shape= (64,))


#instead of using sequential linear layers (.add), use a variable to save layer as a function

dense_1 = layers.Dense(32,activation ='relu')
dense_2 = layers.Dense(32, activation ='relu')
dense_3 = layers.Dense(10, activation ='softmax')

output_tensor(dense_3(dense_2(dense_1(input_tensor))))
