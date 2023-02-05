import os
import cv2

import numpy \
    as np

from configuration \
    import variables

# Globals
training_set = []
test_set = []
validation_set = []

y_training_set = None
y_test_set = None
y_validation_set = None

normalised_training_set = None
normalised_test_set = None
normalised_validation_set = None


# Static Accessors
def get_y_training_set():
    global y_training_set
    return y_training_set


def set_y_training_set(
        value
) -> None:
    global y_training_set
    y_training_set = value


def get_y_test_set():
    global y_test_set
    return y_test_set


def set_y_test_set(
        value
) -> None:
    global y_test_set
    y_test_set = value


def get_y_validation_set():
    global y_validation_set
    return y_validation_set


def set_y_validation_set(
        value
) -> None:
    global y_validation_set
    y_validation_set = value


def get_normalised_training_set():
    global normalised_training_set
    return normalised_training_set


def set_normalised_training_set(
        value
) -> None:
    global normalised_training_set
    normalised_training_set = value


def get_normalised_test_set():
    global normalised_test_set
    return normalised_test_set


def set_normalised_test_set(
        value
) -> None:
    global normalised_test_set
    normalised_test_set = value


def get_normalised_validation_set():
    global normalised_validation_set
    return normalised_validation_set


def set_normalised_validation_set(
        value
) -> None:
    global normalised_validation_set
    normalised_validation_set = value


def set_train_set(
        values
) -> None:
    global training_set
    training_set = values


def get_train_set():
    global training_set
    return training_set


def get_test_set():
    global test_set
    return test_set


def set_test_set(
        values
) -> None:
    global test_set
    test_set = values


def get_validation_set():
    global validation_set
    return validation_set


def set_validation_set(
        values
) -> None:
    global validation_set
    validation_set = values


def load(
        path: str,
        listed_set: list
) -> None:
    for root, dirs, files \
            in os.walk(path):

        for directory \
                in dirs:
            location = os.path.join(path, directory)

            for image \
                    in os.listdir(location):
                image_path = os.path.join(
                    location,
                    image
                )

                image_array = cv2.imread(image_path)
                image_array = cv2.resize(
                    image_array,
                    (
                        variables.get_image_size_x(),
                        variables.get_image_size_y()
                    )
                )

                listed_set.append(
                    image_array
                )


def load_training_set(
        path: str
):
    load(
        path,
        get_train_set()
    )


def load_test_set(
        path: str
):
    load(
        path,
        get_test_set()
    )


def load_validation_set(
        path: str
):
    load(
        path,
        get_validation_set()
    )


def convert():
    set_normalised_training_set(
        np.array(get_train_set())/255.0
    )
    set_normalised_test_set(
        np.array(get_test_set())/255.0
    )
    set_normalised_validation_set(
        np.array(get_validation_set())/255.0
    )


def debug():
    print(
        len(get_train_set())
    )
    print(
        len(get_test_set())
    )
    print(
        len(get_validation_set())
    )

