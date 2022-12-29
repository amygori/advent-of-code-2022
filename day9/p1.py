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
    current_head = start
    current_tail = start
    tail_positions.add(start)
    head_x, head_y = current_head
    tail_x, tail_y = current_tail
    for motion in input:
        direction = motion[0]
        moves = int(motion[2:])
        for _ in range(moves):
            head_x, head_y = move_one(direction, head_x, head_y)
            x_diff = head_x - tail_x
            y_diff = head_y - tail_y

            if abs(x_diff) > 1 or abs(y_diff) > 1:
                if abs(x_diff) == 0 or abs(y_diff) == 0: # they are in the same row or column
                  tail_x, tail_y = move_one(direction, tail_x, tail_y)
                else:  # move diagonally
                  if head_x > tail_x and head_y > tail_y: # move right and up
                      tail_x += 1
                      tail_y += 1
                  elif head_x > tail_x and head_y < tail_y: # move right and down
                      tail_x += 1
                      tail_y -= 1
                  elif head_x < tail_x and head_y < tail_y: # move left and down
                      tail_x -= 1
                      tail_y -= 1
                  elif head_x < tail_x and head_y > tail_y: # move left and up
                      tail_x -= 1
                      tail_y += 1

                tail_positions.add((tail_x, tail_y))

    return len(tail_positions)

if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file).splitlines()
        print(simulate_rope_movement(input))
    else:
        raise TypeError("This is not a file")
