#!/usr/bin/python3
import sys


if __name__ == "__main__":
  print("Starting validation")
  if len(sys.argv) < 2:
    raise RuntimeError("Missing input argument.")
  with open(sys.argv[1]) as input_file:
    print(input_file.read())
  
  pass