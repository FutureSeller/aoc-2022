BASE = ord('a')

def solve(value, window_size):
  start = 0
  end = 0
  
  window_counter = [0] * 26
  for i in range(window_size):
    window_counter[ord(value[i]) - BASE] += 1

  if window_counter.count(1) == window_size:
    return window_size

  start, end = 0, window_size
  while start <= len(value) - window_size:
    window_counter[ord(value[start]) - BASE] -= 1
    window_counter[ord(value[end]) - BASE] += 1

    if window_counter.count(1) == window_size:
      break

    start += 1
    end += 1

  return end + 1

def solution(inputs):
  value = inputs[0]
  return [solve(value, 4), solve(value, 14)]