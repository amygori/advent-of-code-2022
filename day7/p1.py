import sys
from pathlib import Path
import re


class RootNode(object):
    _instance = None

    def __new__(cls):
        # if there is already an instance don't create another one
        if cls._instance is None:
          cls._instance = super(RootNode, cls).__new__(cls)
          cls._instance.parent = None
        return cls._instance

    def __repr__(self) -> str:
        return "/"


class Directory:
  def __init__(self, name, parent):
      self.parent=parent
      self.name = name

  def __repr__(self):
      return f"dir {self.name}"


class File:
  def __init__(self, size, parent, name):
      self.size = size
      self.parent = parent
      self.name= name

  def __repr__(self):
      return f"file {self.name} size={self.size}"


def calculate_total_sizes(output):
    print(input)
    tree_objects = {}
    # start at the root
    wd = RootNode()
    prev_wd = None
    tree_objects['/']=RootNode()
    for index, line in enumerate(output):
      # check command
      if match_cd(line): # matches cd
          argument=re.match(r'(^\$\scd\s)(.*)', line).group(2)
          print("cd to", argument)
          if argument == '..':
              # change directory to parent of wd
              # if we change directory record previous directory
              wd = wd.parent
          elif argument == '/':
              # change directory to root
              print("ROOT")
              wd = RootNode()
          else:
            # get or create directory
            dir = tree_objects.get(argument)
            if dir is None:
                dir = Directory(name=argument, parent=wd)
                tree_objects[dir.name] = dir
            # change working directory
            wd = dir
      elif match_dir(line):
          # create a directory object
          dir_name = re.match(r'(^dir\s)(\w*)', line).group(2)
          print(f"dir {dir_name}")
      elif match_file(line):
            size = re.match(r'^\d+', line).group()
            name = re.match(r'(^\d*\s)(\w*.?\w*)', line).group(2)
            print(f"File name={name} size={size}")
            file = File(name=name, size=size, parent=wd)
            tree_objects[file.name] = file

    print_tree(tree_objects)

def print_tree(tree):
    for key, node in tree.items():
          print("------")
          print(node)
          print("parent:", node.parent)

def match_file(line):
    return re.match(r'^\d+', line)


def match_dir(line):
    return re.match(r'^dir', line)


def match_cd(line):
  return re.match(r'^\$\scd\s.', line)


def match_ls(line):
    return re.match(r'^\$\sls*', line)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file).splitlines()
        calculate_total_sizes(input)
    else:
        raise TypeError("This is not a file")
