def part1(inputs):
  answer = 0
  for line in inputs:
    s1, s2 = line.replace('\n', '').split(',')
    s1_start, s1_end = map(int, s1.split('-'))
    s2_start, s2_end = map(int, s2.split('-'))

    if (s1_start <= s2_start and s2_end <= s1_end) or (s2_start <= s1_start and s1_end <= s2_end):
      answer += 1

  return answer

def part2(inputs):
  answer = 0
  for line in inputs:
    s1, s2 = line.replace('\n', '').split(',')
    s1_start, s1_end = map(int, s1.split('-'))
    s2_start, s2_end = map(int, s2.split('-'))

    if s1_end >= s2_start and s2_end >= s1_start:
      answer += 1

  return answer

def solution(inputs):
  return [part1(inputs), part2(inputs)]