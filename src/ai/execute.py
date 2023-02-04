from keras.applications import VGG19

from keras.applications.vgg19 import preprocess_input
from keras.preprocessing import image

from keras.layers import Flatten, Dense
from tensorflow.python.keras.models import Sequential, Model

import loader


def run():
    vgg_model = VGG19(
        input_shape=(224, 224, 3),
        weights='imagenet',
        include_top=False
    )

    for layer in vgg_model.layers:
        layer.trainable = False

    x = Flatten()(vgg_model.output)
    prediction = Dense(3, activation='softmax')(x)

    model = Model(
        inputs=vgg_model.inputs,
        outputs=prediction
    )

    model.compile(
        loss='sparse_categorical_crossentropy',
        optimizer="adam",
        metrics=['accuracy']
    )

    history = model.fit(
        loader.get_normalised_training_set(),
        loader.get_y_training_set(),
        validation_data=(
            loader.get_normalised_validation_set(),
            loader.get_y_validation_set()
        ),
        epochs=10,
        batch_size=32,
        shuffle=True
    )

    vgg_model.summary()
