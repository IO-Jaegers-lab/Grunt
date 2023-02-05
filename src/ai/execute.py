from keras.applications \
    import VGG19

from keras.layers \
    import \
    Flatten, \
    Dense
from keras.losses import SparseCategoricalCrossentropy

from tensorflow.python.keras.models \
    import Model

import datetime

from configuration \
    import variables

import loader


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
        loss=SparseCategoricalCrossentropy(
            from_logits=True
        ),
        optimizer="adam",
        metrics=[
            'accuracy'
        ],
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

    print("==========================================================================================")
    vgg_model.summary()
    print("Done ====================================================================================")

