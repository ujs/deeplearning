from keras import Input, layers
input_tensor = Input(shape= (64,))


#instead of using sequential linear layers (.add), use a variable to save layer as a function

x = layers.Dense(32,activation ='relu')(input_tensor)
x = layers.Dense(32, activation ='relu')(x)
output_tensor = layers.Dense(10, activation ='softmax')(x)

model = Model(input_tensor, output_tensor)  #instatiating a model. like magic- behind the scenes, keras retrives the flow from input to output via layers
