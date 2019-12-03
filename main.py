#!python

# Work in progress

with open('input_3_test.txt', 'r') as file:
  instructions = []
  grid = print_grid(grid_maker(300, 300))
  for index, line in enumerate(file):
    instructions.append(line.split(sep=","))
  grid_start = [0, 0]
  grid_wire_one = [[0,0]]
  grid_wire_two = [[0,0]]
  for index, instruction in enumerate(instructions[0]):
    prev_x = grid_wire_one[index][0]
    prev_y = grid_wire_one[index][1]

    if instruction[0] == 'L':
      # Left, means X-
      grid_wire_one.append([prev_x - int(instruction[1:]), prev_y])
    if instruction[0] == 'R':
      # Right, means X+
      grid_wire_one.append([prev_x + int(instruction[1:]), prev_y])
    if instruction[0] == 'D':
      # Down, means Y-
      grid_wire_one.append([prev_x, prev_y - int(instruction[1:])])
    if instruction[0] == 'U':
      # Up, means Y+
      grid_wire_one.append([prev_x, prev_y + int(instruction[1:])])

  for index, instruction in enumerate(instructions[1]):
    prev_x = grid_wire_two[index][0]
    prev_y = grid_wire_two[index][1]

    if instruction[0] == 'L':
      # Left, means X-
      grid_wire_two.append([prev_x - int(instruction[1:]), prev_y])
    if instruction[0] == 'R':
      # Right, means X+
      grid_wire_two.append([prev_x + int(instruction[1:]), prev_y])
    if instruction[0] == 'D':
      # Down, means Y-
      grid_wire_two.append([prev_x, prev_y - int(instruction[1:])])
    if instruction[0] == 'U':
      # Up, means Y+
      grid_wire_two.append([prev_x, prev_y + int(instruction[1:])])

  grids = grid_wire_one + grid_wire_two
  crosses = list(set(tuple(x) for x in grids))
  distances = []
  for crossing in crosses:
    if crossing == (0, 0):
      continue
    manhattan = abs(0 - crossing[0]) + abs(0 - crossing[1])
    distances.append(manhattan)
  distances.sort()