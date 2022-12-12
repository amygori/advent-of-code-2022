import sys
from pathlib import Path
import re


SIZE_LIMIT = 100000


class RootNode(object):
    _instance = None

    def __new__(cls):
        # if there is already an instance don't create another one
        if cls._instance is None:
            cls._instance = super(RootNode, cls).__new__(cls)
            cls._instance.parent = None
            cls._instance.type = "dir"
            cls._instance.children = []
            cls._instance.size = 0
            cls._instance.name = "/"
        return cls._instance

    def __repr__(self) -> str:
        return "RootNode /"


class Directory:
    def __init__(self, name, parent):
        self.parent = parent
        self.name = name
        self.type = "dir"
        self.size = 0
        self.children = []

    def __repr__(self):
        return f"dir {self.name} size={self.size}"

    def __str__(self):
        return self.name


class File:
    def __init__(self, size, parent, name):
        self.size = size
        self.parent = parent
        self.name = name
        self.type = "file"
        self.children = None

    def __repr__(self):
        return f"file {self.name} size={self.size} parent={self.parent}"


def create_tree(output):
    for index, line in enumerate(output):
        if match_cd(line):
            directory = re.match(r"(^\$\scd\s)(.*)", line).group(2)
            print("cd to", directory)
            if directory == "..":
                current_dir = current_dir.parent
            elif directory == "/":
                root = RootNode()
                current_dir = root
            else:
                directory = get_or_create_dir(directory, current_dir)
                add_to_tree(directory, current_dir)
                current_dir = directory
        elif match_dir(line):
            dir_name = re.match(r"(^dir\s)(\w*)", line).group(2)
            directory = get_or_create_dir(dir_name, current_dir)
            add_to_tree(directory, current_dir)
        elif match_file(line):
            size = re.match(r"^\d+", line).group()
            name = re.match(r"(^\d*\s)(\w*.?\w*)", line).group(2)
            file = create_file(name, size, current_dir)
            add_to_tree(file, current_dir)
    calculate_sizes(root)
    print("🎄 TOTAL 🎄")
    print(get_sum_of_directories_under_limit(root))


def add_to_tree(object, parent):
    """Add child nodes to parent"""
    if object.name not in [child.name for child in parent.children]:
        parent.children.append(object)


def get_or_create_dir(dir_name, parent):
    if dir_name in [child.name for child in parent.children]:
        return next(
            (child for child in parent.children if child.name == dir_name), None
        )
    return Directory(name=dir_name, parent=parent)


def create_file(file_name, size, parent):
    return File(name=file_name, size=int(size), parent=parent)


def calculate_sizes(object, total=0):
    if object.children is None:
        return object.size
    if len(object.children) < 1:
        object.size += total
        return int(object.size)
    sum_size = sum([calculate_sizes(child, total) for child in object.children])
    object.size += sum_size
    return int(object.size)


def get_sum_of_directories_under_limit(object, total=0):
    for child in [child for child in object.children if (child.type == "dir")]:
        if child.size <= SIZE_LIMIT:
            total += child.size
        if child.type == "dir":
            total = get_sum_of_directories_under_limit(child, total)
    return total


def calculate_size_of_files(directory, size=0):
    size = sum(
        [int(content.size) for content in directory.children if content.type == "file"]
    )
    directory.size = size


def match_file(line):
    return re.match(r"^\d+", line)


def match_dir(line):
    return re.match(r"^dir", line)


def match_cd(line):
    return re.match(r"^\$\scd\s", line)


def match_ls(line):
    return re.match(r"^\$\sls*", line)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file).splitlines()
        create_tree(input)
    else:
        raise TypeError("This is not a file")
