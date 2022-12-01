import sys
import os
import importlib

def main(day_number):
  input_filename = './inputs/%s' % day_number

  if not os.path.isfile(input_filename):
    print ("error: invalid day_number or input file does not exist.")
    exit()

  input_file = open(input_filename, 'r')

  module = importlib.import_module("src.%s" % day_number)
  answer = module.solution(input_file.readlines())

  out = open('out', 'w')
  out.write(str(answer))

  out.close()
  input_file.close()

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print ("cli: python3 runner.py [day_number].")
    exit()
  
  day_number = sys.argv[1]
  main(day_number)
