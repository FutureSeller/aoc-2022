PART1_TABLE= {
  "A": {
    "X": 3,
    "Y": 6,
    "Z": 0,
  },
  "B": {
    "X": 0,
    "Y": 3,
    "Z": 6,
  },
  "C": {
    "X": 6,
    "Y": 0,
    "Z": 3
  }
}

# part 1
def part1(inputs):
  answer = 0
  for line in inputs:
    you, me = line.replace('\n', '').split(' ')
    if me == "X":
      answer += 1
    elif me == "Y":
      answer+= 2
    elif me == "Z":
      answer += 3
    answer += PART1_TABLE[you][me]
  return answer

PART2_TABLE= {
  "X": {
    "A": 3,
    "B": 1,
    "C": 2,
  },
  "Y": {
    "A": 1,
    "B": 2,
    "C": 3,
  },
  "Z": {
    "A": 2,
    "B": 3,
    "C": 1,
  }
}

def part2(inputs):
  answer = 0
  for line in inputs:
    you, me = line.replace('\n', '').split(' ')
    if me == "X":
      answer += 0
    elif me == "Y":
      answer+= 3
    elif me == "Z":
      answer += 6
    answer += PART2_TABLE[me][you]
  return answer

def solution(inputs):
  part1_answer = part1(inputs)
  part2_answer = part2(inputs)
  return [part1_answer, part2_answer]