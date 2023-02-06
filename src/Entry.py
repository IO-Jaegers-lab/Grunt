from io.jaegers.grunt.Application \
    import Application


def main():
    app = Application()
    app.initialise()
    app.execute()
    app.garbage_collection()


if __name__ == '__main__':
    main()
