import sys
from pathlib import Path

# rock: A, paper: B, scissors: C
# rock: X, paper: Y, scissors: Z

# wins
# rock defeats scissors -> CX
# scissors defeats paper -> BZ
# paper defeats rock -> AY

# draws
# AX, BY, CZ

scores = {"X": 1, "Y": 2, "Z": 3, "draw": 3, "win": 6, "lose": 0}


def play_rock_paper_scissors(input):
    total_score = 0
    rounds = [round.replace(" ", "") for round in input]
    for round in rounds:
        outcome = determine_outcome(round)
        total_score += calculate_score(round[1], outcome)
    print(total_score)


def calculate_score(shape, outcome):
    return scores[shape] + scores[outcome]


def determine_outcome(round):
    if round in ["AX", "BY", "CZ"]:
        outcome = "draw"
    elif round in ["CX", "BZ", "AY"]:
        outcome = "win"
    else:
        outcome = "lose"
    return outcome


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file).splitlines()
        play_rock_paper_scissors(input)
    else:
        raise TypeError("This is not a file")
