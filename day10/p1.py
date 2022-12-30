import sys
from pathlib import Path


def start_clock_circuit(input):
    X = 1
    increment_X = 0
    cycle_count = 1
    cycles = {}
    for instructions in input:
        # update X before cycles are incremented again
        X += increment_X
        increment_X = 0  # Reset amount
        instruction = instructions[:4]
        value = int(instructions[5:]) if instructions[5:] else 0
        match (instruction):
            case "addx":
                # create first cycle and record value of X
                cycles[cycle_count] = X
                # increment cycle count
                cycle_count += 1
                # create second cycle and record value of X
                cycles[cycle_count] = X
                # increment cycle count
                cycle_count += 1
            case "noop":
                # record cycle
                cycles[cycle_count] = X
                # then increment cycle
                cycle_count += 1
        increment_X = value  # record amount to add to X
    # account for update after last cycle runs
    X += increment_X
    cycles[cycle_count - 1] = X
    return sum_signals(cycles)


def sum_signals(cycles):
    selected_cycles = range(20, len(cycles) - 1, 40)
    return sum([(cycles[cycle] * cycle) for cycle in selected_cycles])


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file).splitlines()
        print(start_clock_circuit(input))
    else:
        raise TypeError("This is not a file")
