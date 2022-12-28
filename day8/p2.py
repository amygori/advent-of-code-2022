import sys
from pathlib import Path
import math

def edge_count(x_boundary, y_boundary):
    return (x_boundary * 2) + ((y_boundary * 2))


def find_scenic_score(all_trees):
    x = len(all_trees[0])
    y = len(all_trees)
    x_boundary = len(all_trees[0]) - 1
    y_boundary = len(all_trees) - 1
    count = 0
    # account for edges
    count += edge_count(x_boundary, y_boundary)
    all_scenic_scores = []
    for row, trees in enumerate(all_trees):
        if (
            row == 0 or row == y_boundary
        ):  # skip first row and last 2 rows, since we're comparing pairs of trees
            continue
        for column, current_tree in enumerate(trees):
            if (
                column > x_boundary - 1 or column == 0
            ):  # skip first column and last 2 since we are comparing pairs of trees
                continue
            # get all trees between current tree and edge
            trees_to_the_left = [
                all_trees[row][column - index] for index in range(1, column + 1)
            ]
            trees_to_the_right = [
                all_trees[row][column + index] for index in range(1, x - column)
            ]
            trees_above = [
                all_trees[row - index][column] for index in range(1, row + 1)
            ]
            trees_below = [
                all_trees[row + index][column] for index in range(1, y - row)
            ]

            scores = []
            adjacent_trees = [trees_above, trees_to_the_left, trees_to_the_right, trees_below]
            counts = []
            for trees in adjacent_trees:
                count = 0
                for tree in trees:
                    count += 1
                    if tree >= current_tree:
                        break
                counts.append(count)
            score = math.prod(counts)
            scores.append(score)
            all_scenic_scores.append(scores)

    return max(all_scenic_scores)[0]


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file).splitlines()
        print(find_scenic_score(input))
    else:
        raise TypeError("This is not a file")
