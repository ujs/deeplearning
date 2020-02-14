from keras import Input, layers
input_tensor = Input(shape= (32,))


#instead of using sequential linear layers (.add), use a variable to save layer as a function
