from keras import Input, layers
input_tensor = Input(shape= (64,))


#instead of using sequential linear layers (.add), use a variable to save layer as a function

x = layers.Dense(32,activation ='relu')(input_tensor)
x = layers.Dense(32, activation ='relu')(x)
output_tensor = layers.Dense(10, activation ='softmax')(x)

model = Model(input_tensor, output_tensor)  #instatiating a model. like magic- behind the scenes, keras retrives the flow from input to output via layers


from keras import layers
branch_a = layers.Conv2D(128, 1,
activation='relu', strides=2)(x)
branch_b = layers.Conv2D(128, 1, activation='relu')(x)
branch_b = layers.Conv2D(128, 3, activation='relu', strides=2)(branch_b)
branch_c = layers.AveragePooling2D(3, strides=2)(x)
branch_c = layers.Conv2D(128, 3, activation='relu')(branch_c)
branch_d = layers.Conv2D(128, 1, activation='relu')(x)
branch_d = layers.Conv2D(128, 3, activation='relu')(branch_d)
branch_d = layers.Conv2D(128, 3, activation='relu', strides=2)(branch_d)
output = layers.concatenate(
[branch_a, branch_b, branch_c, branch_d], axis=-1)
