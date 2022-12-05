import re

def parse_input(inputs):
  stack_inputs, operation_inputs = inputs[:8], inputs[10:]
  stacks = [[], [], [], [], [], [], [], [], []]

  for index in range(len(stack_inputs)-1, -1, -1):
    stack_cursor = 0
    for j in range(len(stack_inputs[index])):
      if j % 4 == 1:
        if "A" <= stack_inputs[index][j] and "Z" >= stack_inputs[index][j]:
          stacks[stack_cursor].append(stack_inputs[index][j])
        stack_cursor += 1

  operations = []      
  for line in operation_inputs:
    operations.append(list(map(int, re.findall(r'\d+', line))))

  return [stacks, operations]


def part1(inputs):
  stacks, operations = parse_input(inputs)

  for op in operations:
    count, fr, to = op
    while count > 0:
      if stacks[fr - 1]:
        stacks[to - 1].append(stacks[fr - 1].pop())
      count -= 1

  return ''.join(map(list.pop, stacks))

def part2(inputs):
  stacks, operations = parse_input(inputs)

  for op in operations:
    count, fr, to = op
    values = []
    while count > 0:
      if stacks[fr - 1]:
        values.append(stacks[fr - 1].pop())
      count -= 1
    stacks[to - 1] += reversed(values)
    
  return ''.join(map(list.pop, stacks))

def solution(inputs):
  return [part1(inputs), part2(inputs)]
