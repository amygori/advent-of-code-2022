import sys
from pathlib import Path
import re


def find_fully_containing_ranges(input):
    count = 0
    for pairs in input:
        if (
            first_elf_range_start(pairs) <= second_elf_range_start(pairs)
            and first_elf_range_end(pairs) >= second_elf_range_end(pairs)
        ) or (
            second_elf_range_end(pairs) >= first_elf_range_end(pairs)
            and second_elf_range_start(pairs) <= first_elf_range_start(pairs)
        ):
            count += 1
    print(count)


def first_elf_range_start(pairs):
    return int(re.match(r"^\w*", pairs).group())


def first_elf_range_end(pairs):
    return int(re.match(r"(^\w*-)(\w*)", pairs).group(2))


def second_elf_range_start(pairs):
    return int(re.search(r"(\w*,)(\w*)", pairs).group(2))


def second_elf_range_end(pairs):
    return int(re.search(r"(\w*-)(\w*,)(\w*-)(\w*)", pairs).group(4))


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file).splitlines()
        find_fully_containing_ranges(input)
    else:
        raise TypeError("This is not a file")
