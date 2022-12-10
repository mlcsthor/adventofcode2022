from re import search

interesting_signals = [20 + 40*i for i in range(6)]

def check_cycles(cycles, x):
  return cycles in interesting_signals

def draw_pixels(pixel, x):
  return '#' if pixel in [x, x + 1, x + 2] else '.'

def calc_strengths_sum(lines):
  cycles = 0
  x = 1
  strengths_sum = 0

  for line in lines:
    cycles += 1
    if check_cycles(cycles, x):
      strengths_sum += cycles * x

    if line != 'noop':
      cycles += 1
      if check_cycles(cycles, x):
        strengths_sum += cycles * x

      operation = search("addx (.+)", line)
      if operation:
        value = int(operation.groups()[0])
        x += value

  return strengths_sum

def get_sprite(lines):
  cycles = 0
  x = 1
  pixel = 1
  pixels = []

  for line in lines:
    cycles += 1
    pixels.append(draw_pixels(pixel, x))
    pixel = (pixel + 1)%40

    if line != 'noop':
      cycles += 1
      pixels.append(draw_pixels(pixel, x))
      pixel = (pixel + 1)%40

      operation = search("addx (.+)", line)
      if operation:
        value = int(operation.groups()[0])
        x += value

  for i in range(6):
    print(''.join(pixels[40*i:40*(i+1) - 1]))

print('### Advent of Code Day 10 ###\n')

with open('example.txt') as file:
  lines = [line.strip() for line in file.readlines()]
  strengths_sum = calc_strengths_sum(lines)
  print(f'Example for Part 1: {strengths_sum}')
  print(f'Example for Part 2:')
  get_sprite(lines)

with open('input.txt') as file:
  lines = [line.strip() for line in file.readlines()]
  strengths_sum = calc_strengths_sum(lines)
  print(f'\nAnswer for Part 1: {strengths_sum}')
  print(f'Answer for Part 2:')
  get_sprite(lines)