import sys
from pathlib import Path
import string


def find_priority_total(input):
    total = 0
    for content in input:
        half = len(content) // 2
        first_compartment, second_compartment = set(content[:half]), set(content[half:])
        common_item = first_compartment.intersection(second_compartment)
        priority = string.ascii_letters.index(common_item.pop()) + 1
        total += priority
    print(total)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file).splitlines()
        find_priority_total(input)
    else:
        raise TypeError("This is not a file")
