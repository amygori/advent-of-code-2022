import sys
from pathlib import Path
from collections import deque


def rearrange_crates(crates, moves):
    stacks = parse_stacks(crates)
    print(stacks)
    # print("🏗️  MOVES ")
    # print(moves)


def parse_stacks(crates_string):
    # create a list of strings for each line in crate data
    crates = crates_string.split("\n")
    # create dictionary with keys from the last line of crate data
    stack_labels = crates[-1].replace(" ", "")
    stacks = {}
    for num in stack_labels:
        stacks[int(num)] = []
    # remove the last row once we've used it for labels
    crates.pop()
    # create a place to store rows of crates that can be moved
    crate_grid = deque()
    for index, crate_row in enumerate(crates):
        # normalize the string so the index positions line up with the stacks
        crate_row = (
            crate_row.replace("[", "")  # remove brackets
            .replace("]", "")
            .replace("    ", "X") # insert "X" as placeholder for empty spot, look for 4 spaces
            .replace(" ", "") # remove remaining whitepace
        )
        # if the length of the row is less than the total len of the keys we put in the dict,
        # then we are missing a trailing X.
        if len(crate_row) < len(stacks.keys()):
          crate_row += "X"
        crate_grid.appendleft(crate_row)
    # loop through crates and put them into the lists in the dictionary
    for crate_row in crate_grid:
        for index, crate in enumerate(crate_row): # 'ZMP' - z goes on the bottom of stack 1, m on the bottom of stack 2, and p on the
            if crate == "X":
                continue
            stacks[index + 1].append(crate)
    return stacks



if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        crates, moves = Path.read_text(file).rstrip().split("\n\n")
        rearrange_crates(crates, moves)
    else:
        raise TypeError("This is not a file")
