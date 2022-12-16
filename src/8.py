from functools import reduce

def parse_input(inputs):
  row = len(inputs)
  col = len(inputs[0].rstrip())
  board = [[0] * col for _ in range(row)]
  for i in range(row):
    for j in range(col):
      board[i][j] = int(inputs[i][j])
  return board

def part1(board):
  row = len(board)
  col = len(board[0])
  visible_board = [[False] * col for _ in range(row)]
  for i in range(col):
    visible_board[0][i] = visible_board[row-1][i] = True
  for i in range(row):
    visible_board[i][0] = visible_board[i][row-1] = True

  col_index = 1
  while col_index < col - 1:
    max_top = board[0][col_index]
    for j in range(1, row-1):
      if max_top < board[j][col_index]:
        max_top = board[j][col_index]
        visible_board[j][col_index] = True
    col_index += 1

  col_index = 1
  while col_index < col - 1:
    max_bottom = board[row-1][col_index]
    for j in range(row-1, -1, -1):
      if max_bottom < board[j][col_index]:
        max_bottom = board[j][col_index]
        visible_board[j][col_index] = True
    col_index += 1

  row_index = 1
  while row_index < row - 1:
    max_left = board[row_index][0]
    for j in range(1, col-1):
      if max_left < board[row_index][j]:
        max_left = board[row_index][j]
        visible_board[row_index][j] = True
    row_index += 1

  row_index = 1
  while row_index < row - 1:
    max_right = board[row_index][col-1]
    for j in range(col-1, -1,-1):
      if max_right < board[row_index][j]:
        max_right = board[row_index][j]
        visible_board[row_index][j] = True
    row_index += 1

  return sum([row.count(True) for row in visible_board])

def compute_score(value, route):
  score = 0
  for r in route:
    score += 1
    if r >= value:
      break
  return score

def part2(board):
  row = len(board)
  col = len(board[0])
  visible_board = [[0] * col for _ in range(row)]

  for i in range(1, row-1):
    for j in range(1, col-1):
      routes = [
        reversed(board[i][:j]),
        board[i][j+1:],
        [board[row][j] for row in range(i-1, -1, -1)],
        [board[row][j] for row in range(i+1, row)]
      ]
      visible_board[i][j] = reduce(
        lambda x,y: x*y, 
        list(
          map(lambda route: compute_score(board[i][j], route), routes)
        )
      )

  return max([max(row) for row in visible_board])

def solution(inputs):
  board = parse_input(inputs)
  return [part1(board), part2(board)]