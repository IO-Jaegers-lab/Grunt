import wandb
from keras.preprocessing.image import ImageDataGenerator
import loader
import execute


wandb.init(
    project="test-project",
    entity="io-jaegers"
)

root = '/mnt/d/dataset/Filtered'

test_path = root + r'/Test'
train_path = root + r'/Training'
validation_path = root + r'/Validation'


def main() -> None:
    global \
        train_path, \
        test_path, \
        validation_path

    loader.load_training_set(train_path)
    loader.load_test_set(test_path)
    loader.load_validation_set(validation_path)
    loader.debug()

    # Normalise Set
    loader.convert()

    train_datagen = ImageDataGenerator(
        rescale=1./255
    )

    training_set = train_datagen.flow_from_directory(
        train_path,
        target_size=(224, 224),
        batch_size=32,
        class_mode="sparse"
    )

    print("training set:")
    print(training_set.class_indices)

    test_datagen = ImageDataGenerator(
        rescale=1./255
    )
    test_set = test_datagen.flow_from_directory(
        test_path,
        target_size=(224, 224),
        batch_size=32,
        class_mode="sparse"
    )

    print("test set:")
    print(test_set.class_indices)

    validation_datagen = ImageDataGenerator(
        rescale=1./255
    )
    validation_set = validation_datagen.flow_from_directory(
        validation_path,
        target_size=(224, 224),
        batch_size=32,
        class_mode="sparse"
    )

    print("validation set:")
    print(validation_set.class_indices)

    loader.set_y_training_set(training_set.classes)
    loader.set_y_test_set(test_set.classes)
    loader.set_y_validation_set(validation_set.classes)

    execute.run()




if __name__ == '__main__':
    main()