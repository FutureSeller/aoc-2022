def get_ord_alphabet(char):
  value = ord(char)
  if ord('a') <= value <= ord('z'):
    return value - ord('a') + 1
  return value - ord('A') + 27

def part1(inputs):
  answer = 0
  for line in inputs:
    _line = line.replace('\n', '')
    length = len(_line) // 2
    first_rucksack = _line[:length]
    second_rucksack = _line[length:]

    char_dict = {}
    for char in first_rucksack:
      char_dict[char] = char_dict.get(char, 0) + 1
    
    for char in second_rucksack:
      if char in char_dict:
        break

    answer += get_ord_alphabet(char)
  return answer

def part2(inputs):
  length = len(inputs)
  if length % 3 != 0:
    raise Exception('invalid inputs.')

  answer = 0
  for i in range(0, len(inputs), 3):
    first_line = inputs[i].replace('\n', '')
    second_line = inputs[i + 1].replace('\n', '')
    third_line = inputs[i + 2].replace('\n', '')

    char_dict = {}
    for char in first_line:
      if char not in char_dict:
        char_dict[char] = set()
      char_dict[char].add(1)

    for char in second_line:
      if char not in char_dict:
        char_dict[char] = set()
      char_dict[char].add(2)

    for char in third_line:
      if char not in char_dict:
        char_dict[char] = set()
      char_dict[char].add(3)

    for char, item in char_dict.items():
      if len(item) == 3:
        answer += get_ord_alphabet(char)
        break
    
  return answer

def solution(inputs):
  return [part1(inputs), part2(inputs)]