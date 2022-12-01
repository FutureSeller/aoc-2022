def solution(inputs):
  max_calory = -1
  prev_calory = 0

  for line in inputs:
    if line == '\n':
      max_calory = max_calory if max_calory > prev_calory else prev_calory
      prev_calory = 0
      continue
    prev_calory += int(line.replace('\n', ''))

  return max_calory