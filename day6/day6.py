import sys
from pathlib import Path


def find_marker_position(chars, length):
    for index in range(0, len(chars)):
        possible_marker_position = index + length
        substr = chars[index:possible_marker_position]
        charset = set(substr)
        if len(charset) == len(substr):
            return possible_marker_position


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file)
        length_part_1 = 4
        length_part_2 = 14
        print(find_marker_position(input, length_part_2))
    else:
        raise TypeError("This is not a file")
