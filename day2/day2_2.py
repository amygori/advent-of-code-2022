import sys
from pathlib import Path

# rock: A, paper: B, scissors: C
# lose: X, draw: Y, win: Z

scores = {"X": 0, "Y": 3, "Z": 6, "A": 1, "B": 2, "C": 3}


def play_rock_paper_scissors(input):
    total_score = 0
    rounds = [round.replace(" ", "") for round in input]
    for round in rounds:
        outcome_score = scores[round[1]]
        round_with_shape = add_shape_for_required_outcome(round)
        total_score += calculate_score(round_with_shape[2], outcome_score)
    print(total_score)


def calculate_score(shape, outcome_score):
    return scores[shape] + outcome_score


def add_shape_for_required_outcome(round):
    required_outcome = round[1]
    if required_outcome == "X":  # lose
        # look up the required shape
        shape_to_lose = {"A": "C", "C": "B", "B": "A"}
        round += shape_to_lose[round[0]]
    elif required_outcome == "Z":  # win
        shape_to_win = {"A": "B", "B": "C", "C": "A"}
        round += shape_to_win[round[0]]
    else:  # draw
        round += round[0]
    return round


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file).splitlines()
        play_rock_paper_scissors(input)
    else:
        raise TypeError("This is not a file")
