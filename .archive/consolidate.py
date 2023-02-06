import os
import shutil

path = r'D:\dataset\all images\Photographs\From\Old'


def main() -> None:
    global path
    counter = 0

    for root, dirs, files in os.walk(path, topdown=False):
        for file in files:
            counter = counter + 1
            fp = os.path.join(root, file)
            filename_complete = str(counter) + '.' + file
            moved_to = os.path.join(path, filename_complete)
            shutil.move(fp, moved_to)


if __name__ == '__main__':
    main()