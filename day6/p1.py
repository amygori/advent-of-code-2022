import sys
from pathlib import Path


def find_marker_position(chars):
    for index in range(0, len(chars)):
    # check successive sets of 4 chars
        possible_marker_position = index + 4
        substr = chars[index:possible_marker_position]
        charset = set(substr)
        if len(charset) == len(substr):
            return possible_marker_position


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file)
        print(find_marker_position(input))
    else:
        raise TypeError("This is not a file")
