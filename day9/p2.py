import sys
from pathlib import Path

def move_one(direction, x, y):
    match direction:
          case "R":
              x += 1
          case "L":
              x -= 1
          case "U":
              y += 1
          case "D":
              y -= 1
    return (x, y)

def simulate_rope_movement(input):
    tail_positions = set()
    start = (0, 0)

    ROPE_LENGTH = 10
    knots = []
    for _ in range(ROPE_LENGTH):
        knots.append(start)

    for motion in input:
        direction = motion[0]
        moves = int(motion[2:])
        for iteration in range(moves):
            head_x, head_y = knots[0]
            head_x, head_y = move_one(direction, head_x, head_y)
            knots[0] = (head_x, head_y)
            for i in range(1, len(knots)):
                knot_x, knot_y = knots[i]

                previous_knot_x, previous_knot_y = knots[i-1]
                x_diff = previous_knot_x - knot_x
                y_diff = previous_knot_y - knot_y

                if abs(x_diff) > 1 or abs(y_diff) > 1:
                    if abs(y_diff) == 0: # they are in the same row
                      if previous_knot_x > knot_x: # move right
                        knot_x += 1
                      else: # move left
                        knot_x -= 1
                    elif abs(x_diff) == 0: #they are in the same column
                      if previous_knot_y > knot_y: # move up
                          knot_y += 1
                      else: # move down
                          knot_y -= 1
                    else:  # move diagonally
                      if previous_knot_x > knot_x and previous_knot_y > knot_y: # move right and up
                          knot_x += 1
                          knot_y += 1
                      elif previous_knot_x > knot_x and previous_knot_y < knot_y: # move right and down
                          knot_x += 1
                          knot_y -= 1
                      elif previous_knot_x < knot_x and previous_knot_y < knot_y: # move left and down
                          knot_x -= 1
                          knot_y -= 1
                      elif previous_knot_x < knot_x and previous_knot_y > knot_y: # move left and up
                          knot_x -= 1
                          knot_y += 1
                    knots[i] = (knot_x, knot_y)
                #replace the knot in the list at the right index position
                if i == len(knots) - 1: # if this is the last knot
                    tail_positions.add(knots[i])

    return len(tail_positions)

if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file).splitlines()
        print(simulate_rope_movement(input))
    else:
        raise TypeError("This is not a file")
