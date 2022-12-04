from typing import TextIO

def get_assignments(file: TextIO) -> list[list]:
  assignments = []

  for line in file.readlines():
    sections = []
    pairs = line.strip().split(',')

    for pair in pairs:
      pair = pair.split('-')
      sections.append(list(range(int(pair[0]), int(pair[1]) + 1)))

    assignments.append(sections)

  return assignments

def get_overlapping(assignments: list[list]) -> int:
  overlapping: int = 0

  for assignment in assignments:
    check1 = all(item in assignment[0] for item in assignment[1])
    check2 = all(item in assignment[1] for item in assignment[0]) 
    check = check1 or check2

    if check:
      overlapping += 1

  return overlapping

def get_overlapping_at_all(assignments: list[list]) -> int:
  overlapping: int = 0

  for assignment in assignments:
    check1 = any(item in assignment[0] for item in assignment[1])
    check2 = any(item in assignment[1] for item in assignment[0]) 
    check = check1 or check2

    if check:
      overlapping += 1

  return overlapping

print('### Advent of Code Day 4 ###\n')

with open('example.txt') as file:
  assignments = get_assignments(file)
  overlapping = get_overlapping(assignments)
  print(f'Example for Part 1: {overlapping}')

  overlapping = get_overlapping_at_all(assignments)
  print(f'Example for Part 2: {overlapping}\n')

with open('input.txt') as file:
  assignments = get_assignments(file)
  overlapping = get_overlapping(assignments)
  print(f'Answer for Part 1: {overlapping}')

  overlapping = get_overlapping_at_all(assignments)
  print(f'Answer for Part 2: {overlapping}')