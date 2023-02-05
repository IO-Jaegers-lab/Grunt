import wandb

from keras.preprocessing.image \
    import ImageDataGenerator

from tensorflow.python.eager.context \
    import set_log_device_placement

import loader
import execute

from configuration \
    import variables

set_log_device_placement(True)

root = '/mnt/d/dataset/Filtered'
variables.set_dataset(root)

wandb.init(
    project="test-project",
    entity="io-jaegers"
)

test_path = variables.get_dataset() + r'/Test'
train_path = variables.get_dataset() + r'/Training'
validation_path = variables.get_dataset() + r'/Validation'


def main() -> None:
    global \
        train_path, \
        test_path, \
        validation_path

    loader.load_training_set(
        train_path
    )

    loader.load_test_set(
        test_path
    )

    loader.load_validation_set(
        validation_path
    )

    loader.debug()

    # Normalise Set
    loader.convert()

    train_datagen = ImageDataGenerator(
        rescale=1./255
    )

    training_set = train_datagen.flow_from_directory(
        train_path,
        target_size=(
            variables.get_image_size_x(),
            variables.get_image_size_y()
        ),
        seed=variables.next_seed(),
        batch_size=variables.get_batch_size(),
        class_mode="sparse"
    )

    print("training set:")
    print(training_set.class_indices)

    test_datagen = ImageDataGenerator(
        rescale=1./255
    )
    test_set = test_datagen.flow_from_directory(
        test_path,
        target_size=(
            variables.get_image_size_x(),
            variables.get_image_size_y()
        ),
        seed=variables.next_seed(),
        batch_size=variables.get_batch_size(),
        class_mode="sparse"
    )

    print("test set:")
    print(test_set.class_indices)

    validation_datagen = ImageDataGenerator(
        rescale=1./255
    )

    validation_set = validation_datagen.flow_from_directory(
        validation_path,
        target_size=(
            variables.get_image_size_x(),
            variables.get_image_size_y()
        ),
        seed=variables.next_seed(),
        batch_size=variables.get_batch_size(),
        class_mode="sparse"
    )

    print("validation set:")
    print(validation_set.class_indices)

    loader.set_y_training_set(
        training_set.classes
    )

    loader.set_y_test_set(
        test_set.classes
    )

    loader.set_y_validation_set(
        validation_set.classes
    )

    execute.run()


if __name__ == '__main__':
    main()