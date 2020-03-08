#!/usr/bin/python3
import sys
from scanner import Scanner
from parser import Parser


if __name__ == "__main__":
  file_text = ""
  print("Starting validation")
  if len(sys.argv) < 2:
    raise RuntimeError("Missing input argument.")
  with open(sys.argv[1]) as input_file:
    file_text = input_file.read()
  # print(file_text)

  scanner = Scanner(file_text)
  parser = Parser(scanner)
  parser.start()

  
  pass