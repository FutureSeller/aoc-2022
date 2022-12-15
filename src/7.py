class File:
  def __init__(self, name="", size=0, parent=None):
    self.name = name
    self.size = size
    self.parent = parent

class Directory:
  def __init__(self, name="", parent=None, size=0):
    self.name = name
    self.parent = parent
    self.size = size
    self.subdirs = None
    self.files = {}

  def add_subdir(self, name):
    if self.subdirs == None:
      self.subdirs = {}

    dir = Directory()
    dir.name = name
    dir.parent = self
    self.subdirs[name] = dir

  def get_subdir(self, name):
    return self.subdirs[name]
  
  def add_file(self, name, size):
    self.files[name] = File(name, size, self)
    self.size += size

def parse_inputs(inputs):
  root_dir = Directory()
  cursor = root_dir
  line = 0
  while line < len(inputs):
    argv = inputs[line].rstrip().split()
    if argv[:2] == ["$", "ls"]: pass
    elif argv[:2] == ["$", "cd"]:
      if argv[2] == "/":
        cursor = root_dir
      elif argv[2] == "..":
        cursor = cursor.parent
      else:
        cursor = cursor.get_subdir(argv[2])  
    else:
      if argv[0] == "dir":
        cursor.add_subdir(argv[1])
      else:
        cursor.add_file(argv[1], int(argv[0]))
    line += 1
  return root_dir

def calculate_total_file_size_in_dir(dir):
  if not dir: return 0
  if not dir.subdirs: return dir.size

  for name in dir.subdirs.keys():
    if isinstance(dir.subdirs[name], Directory):
      child_dir_size = calculate_total_file_size_in_dir(dir.subdirs[name])
      dir.size += child_dir_size
  return dir.size

def part1(root_dir):
  numbers = []

  def _solve_part1(dir):
    if not dir: return

    if dir.size <= 100000: 
      numbers.append(dir.size)

    if not dir.subdirs: return

    for name in dir.subdirs.keys():
      if isinstance(dir.subdirs[name], Directory):
        _solve_part1(dir.subdirs[name])

  _solve_part1(root_dir)
  return sum(numbers)

def part2(root_dir):
  TOTAL_SIZE = 70000000
  TO_BE_UNUSED_SIZE = 30000000

  target = TO_BE_UNUSED_SIZE - (TOTAL_SIZE - root_dir.size)
  numbers = []

  def _solve_part2(dir):
    if not dir: return

    if dir.size >= target:
      numbers.append(dir.size)

    if not dir.subdirs: return

    for name in dir.subdirs.keys():
      if isinstance(dir.subdirs[name], Directory):
        _solve_part2(dir.subdirs[name])

  _solve_part2(root_dir)

  return min(sorted(numbers))

def solution(inputs):
  root_dir = parse_inputs(inputs)
  calculate_total_file_size_in_dir(root_dir)
  return [part1(root_dir), part2(root_dir)]
