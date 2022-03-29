import os


class File:
    name: str = None
    text: str = None

    def __init__(self, name: str, text: str = None):
        self.name = name
        self.text = text

    def create(self, parent_path):
        with open(os.path.join(parent_path, self.name), "w") as f:
            pass


class Directory:
    name: str = None
    dirs: list = None
    files: list = None

    def __init__(self, name: str, dirs: list = None, files: list = None):
        self.name = name
        self.dirs = dirs
        self.files = files

    def create(self, parent_path):
        # Create this dir
        path = os.path.join(parent_path, self.name)
        os.mkdir(path)

        # Create the files in this dir
        if self.files is not None:
            for file in self.files:
                file.create(path)

        # Recursively create the dirs in this dir
        if self.dirs is not None:
            for dir in self.dirs:
                dir.create(path)


if __name__ == "__main__":
    base_path = "./"
    base_dir = Directory("first_dir", dirs=[
        Directory("second_level", dirs=None, files=[
            File("test1"),
            File("test2")
        ]),
        Directory("empty_dir", dirs=None, files=None)
    ], files=[
        File("test1"),
        File("test2"),
        File("test3")
    ])

    base_dir.create(base_path)
