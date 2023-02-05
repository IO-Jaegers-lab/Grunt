from keras.applications \
    import VGG19

from keras.layers \
    import \
    Flatten, \
    Dense

from tensorflow.python.keras.models \
    import \
    Model

import loader
from src.ai.configuration import variables


def run():
    vgg_model = VGG19(
        input_shape=(
            variables.get_image_size_x(),
            variables.get_image_size_y(),

            variables.get_image_size_depth()
        ),
        weights='imagenet',

        include_top=False
    )

    for layer in vgg_model.layers:
        layer.trainable = False

    x = Flatten()(vgg_model.output)
    prediction = Dense(
        variables.get_size_of_categories(),
        activation='softmax'
    )(x)

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

        epochs=variables.get_epoch(),
        batch_size=variables.get_batch_size(),

        shuffle=True
    )

    vgg_model.summary()
