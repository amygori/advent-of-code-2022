import sys
from pathlib import Path


def calculate_totals(input):
    total = 0
    max_value = 0
    for amount in input:
      if not amount:
          total = 0
          continue
      total += int(amount)
      if total > max_value:
        max_value = total
    print(max_value)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file).splitlines()
        calculate_totals(input)
    else:
        raise TypeError("This is not a file")
