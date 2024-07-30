from tensorflow.keras.models import Model
from keras.applications import VGG19
import tensorflow as tf
from tensorflow.keras.layers import Dense, Dropout
from config import *
from data_generator import *

def train_vgg():
    base_model = VGG19(weights='imagenet', include_top=False) #imports the VGG19 model and discards the last layer.
    x = base_model.output # (None, None, None, 512)
    x = tf.keras.layers.GlobalAveragePooling2D()(x) # (None, 512)

    x = Dropout(0.2)(x) # (None, 512)
    x = Dense(256,activation='relu')(x) # (None, 256)
    x = Dropout(0.2)(x) # (None, 256)

    preds = Dense(num_classes,activation='softmax')(x) #final layer with softmax activation

    model_vgg = Model(inputs=base_model.input, outputs=preds)

    #Freeze layers from VGG16 backbone (not to be trained)
    for layer in base_model.layers:
        layer.trainable=False

    #model_vgg.summary()

    model_vgg.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    model_vgg.fit(train_generator,
                    steps_per_epoch=steps_per_epoch_training,
                    epochs=num_epochs,
                    validation_data=validation_generator,
                    validation_steps=steps_per_epoch_validation,
                    verbose="auto" )
    
    model_vgg.save('classifier_vgg_model.h5')

    return model_vgg

if __name__ == "__main__":
    pass