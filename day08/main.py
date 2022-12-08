def check_horizontal(grid_part, val) -> bool:
  for elt in grid_part:
    if elt >= val:
      break
  else:
    return True

  return False

def check_vertical(x_idx, y_range, val) -> bool:
  for i in y_range:
    if grid[i][x_idx] >= val:
      break
  else:
    return True

  return False

def calc_visible_trees(grid) -> int:
  already_visible = len(grid)*2 + len(grid[0])*2 - 4
  visible = set()

  for y_idx, _ in enumerate(grid[1:-1], start=1):
    for x_idx, x_val in enumerate(grid[y_idx][1:-1], start=1):
      # Check left
      if check_horizontal(grid[y_idx][0:x_idx], x_val):
        visible.add((y_idx, x_idx))
        continue

      # Check right
      if check_horizontal(grid[y_idx][x_idx+1:], x_val):
        visible.add((y_idx, x_idx))
        continue

      # Check up
      if check_vertical(x_idx, range(y_idx), x_val):
        visible.add((y_idx, x_idx))
        continue

      # Check down
      if check_vertical(x_idx, range(y_idx+1, len(grid)), x_val):
        visible.add((y_idx, x_idx))
        continue

  return len(visible) + already_visible

print('### Advent of Code Day 7 ###\n')

with open('example.txt') as file:
  grid = [list(line.strip()) for line in file.readlines()]
  visible_trees = calc_visible_trees(grid)
  print(f'Example for Part 1: {visible_trees}')

with open('input.txt') as file:
  grid = [list(line.strip()) for line in file.readlines()]
  visible_trees = calc_visible_trees(grid)
  print(f'Answer for Part 1: {visible_trees}')