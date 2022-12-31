import sys
from pathlib import Path


class CRT:
    CRT_HEIGHT = 6
    CRT_WIDTH = 40

    def __init__(self):
        self.rows = {}
        self.current_row_index = 0
        for row in range(self.CRT_HEIGHT):
            self.rows[row] = ""

    def _row_complete(self, row):
        if len(row) == self.CRT_WIDTH:
            return True
        return False

    def draw_pixel(self, sprite, X):
        if self._row_complete(self.rows[self.current_row_index]):
            # if row is complete, then set the next row to the current row
            self.current_row_index += 1
        # choose pixel based on overlap of current pixel and sprite position
        pixel = "#" if len(self.rows[self.current_row_index]) in sprite else "."
        self.rows[self.current_row_index] += pixel


def start_clock_circuit(input):
    X = 1
    increment_X = 0
    cycle_count = 1
    cycles = {}
    sprite = sprite_position(X)
    crt = CRT()

    for instructions in input:
        X += increment_X
        sprite = sprite_position(X)
        increment_X = 0
        instruction = instructions[:4]
        value = int(instructions[5:]) if instructions[5:] else 0
        match (instruction):
            case "addx":
                # first cycle
                crt.draw_pixel(sprite, X)
                cycles[cycle_count] = X
                cycle_count += 1

                # second cycle
                crt.draw_pixel(sprite, X)
                cycles[cycle_count] = X
                cycle_count += 1
            case "noop":
                crt.draw_pixel(sprite, X)
                cycles[cycle_count] = X
                cycle_count += 1
        increment_X = value
    X += increment_X
    cycles[cycle_count - 1] = X

    for row in crt.rows.values():
        print(row)


def sprite_position(X):
    return (X - 1, X, X + 1)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file).splitlines()
        start_clock_circuit(input)
    else:
        raise TypeError("This is not a file")
