from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from config import *
from data_generator import *

def train_cnn():
    input = Input(shape=(image_resize,image_resize,3,)) # (None,224,224,3)

    conv1 = Conv2D(32,(5,5),activation='relu',padding="same")(input) # (None,224,224,32)
    pool1 = MaxPooling2D(pool_size=(2,2))(conv1) # (None,112,112,32)

    conv2 = Conv2D(64,(3,3),activation='relu',padding="same")(pool1) # (None,112,112,64)
    pool2 = MaxPooling2D(pool_size=(2,2))(conv2) # (None,56,56,64)

    conv3 = Conv2D(32,(3,3),activation='relu',padding="same")(pool2) # (None,56,56,32)
    pool3 = MaxPooling2D(pool_size=(2,2))(conv3) # (None,28,28,32)

    conv4 = Conv2D(32,(3,3),activation='relu',padding="same")(pool3) # (None,28,28,32)
    pool4 = MaxPooling2D(pool_size=(2,2))(conv3) # (None,28,28,32)

    conv4 = Conv2D(32,(3,3),activation='relu',padding="same")(pool4) # (None,28,28,64)
    pool4 = MaxPooling2D(pool_size=(2,2))(conv4) # (None,14,14,32)

    flat = Flatten()(pool4) # (None, 6272)

    drop = Dropout(0.2)(flat) # (None, 6272)

    fully = Dense(512,activation='relu')(drop) # (None, 512)
    pred = Dense(num_classes,activation='softmax')(fully) # (None, 2)

    model_cnn = Model(inputs=input, outputs=pred)

    model_cnn.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    train_generator.reset()
    validation_generator.reset()
    model_cnn.fit(train_generator,
                    steps_per_epoch=steps_per_epoch_training,
                    epochs=num_epochs,
                    validation_data=validation_generator,
                    validation_steps=steps_per_epoch_validation,
                    #verbose="auto"
                    )
    model_cnn.save('classifier_cnn_model.h5')
    return model_cnn

if __name__ == "__main__":
    pass