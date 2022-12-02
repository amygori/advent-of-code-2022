import sys
from pathlib import Path


def calculate_totals(input):
    total = 0
    totals=[]
    for index, amount in enumerate(input):
        if amount:
            total += int(amount)
            if index == len(input) - 1:
              totals.append(total)
        else:
          totals.append(total)
          total = 0
          continue
    top_three=sorted(totals)[-3:]
    print(sum(top_three))


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file).splitlines()
        calculate_totals(input)
    else:
        raise TypeError("This is not a file")
