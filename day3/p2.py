import sys
from pathlib import Path
import string


def find_priority_total(input):
    total = 0
    index_value = 0
    for content in input:
        if index_value <= (len(input) - 3):
            first_elf = set(input[index_value])
            second_elf = set(input[index_value + 1])
            third_elf = set(input[index_value + 2])
            common_item = first_elf & second_elf & third_elf
            index_value += 3
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
