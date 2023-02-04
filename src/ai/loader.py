import os
import cv2

import numpy \
    as np

training_set = []
test_set = []
validation_set = []

y_training_set = None
y_test_set = None
y_validation_set = None

normalised_training_set = None
normalised_test_set = None
normalised_validation_set = None


def get_y_training_set():
    global y_training_set
    return y_training_set


def set_y_training_set(value):
    global y_training_set
    y_training_set = value


def get_y_test_set():
    global y_test_set
    return y_test_set


def set_y_test_set(value):
    global y_test_set
    y_test_set = value


def get_y_validation_set():
    global y_validation_set
    return y_validation_set


def set_y_validation_set(value):
    global y_validation_set
    y_validation_set = value

# Static Accessors
def get_normalised_training_set():
    global normalised_training_set
    return normalised_training_set


def set_normalised_training_set(value):
    global normalised_training_set
    normalised_training_set = value


def get_normalised_test_set():
    global normalised_test_set
    return normalised_test_set


def set_normalised_test_set(value):
    global normalised_test_set
    normalised_test_set = value


def get_normalised_validation_set():
    global normalised_validation_set
    return normalised_validation_set


def set_normalised_validation_set(value):
    global normalised_validation_set
    normalised_validation_set = value


def set_train_set(values):
    global training_set
    training_set = values


def get_train_set():
    global training_set
    return training_set


def get_test_set():
    global test_set
    return test_set


def set_test_set(values):
    global test_set
    test_set = values


def get_validation_set():
    global validation_set
    return validation_set


def set_validation_set(values):
    global validation_set
    validation_set = values


def load_training_set(path: str):
    set = get_train_set()

    for folder in os.listdir(path):
        subpath = path + "/" + folder

        for img in os.listdir(subpath):
            image_path = subpath + "/" + img

            image_array = cv2.imread(image_path)
            image_array = cv2.resize(image_array, (224, 224))

            set.append(image_array)


def load_test_set(path: str):
    set = get_test_set()

    for folder in os.listdir(path):
        sub_path = path + "/" + folder

        for img in os.listdir(sub_path):
            image_path = sub_path + "/" + img
            img_array = cv2.imread(image_path)
            img_array = cv2.resize(img_array, (224, 224))

            set.append(img_array)


def load_validation_set(path: str):
    set = get_validation_set()


    for folder in os.listdir(path):
        sub_path = path + "/" + folder

        for img in os.listdir(sub_path):
            image_path = sub_path + "/" + img
            img_array = cv2.imread(image_path)
            img_array = cv2.resize(img_array, (224, 224))

            set.append(img_array)


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
    print(len(get_train_set()))
    print(len(get_test_set()))
    print(len(get_validation_set()))

