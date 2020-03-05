#!/usr/bin/python3
import re as regex
import collections
import sys

Token = collections.namedtuple("Token", ["type", "value", "line", "collumn"])

class Scanner:

  def __init__ (self):
    self.tokens_ = []
    self.current_token_ = 0

  def readKeywords(self):
    with open("keywords") as kw:
      return [word.upper() for word in kw.read().split(sep=",")]

  def readTokenSpecs(self):
    with open("token_specs") as token_specs:
      return [(spec.split(",")[0], spec.split(",")[1].rstrip("\n")) for spec in token_specs.readlines()]

  
  def tokenize(self, input_string):

    pass
  
  def nextToken(self):
    pass

if __name__ == "__main__":
  print("Starting scanner")
  scanner = Scanner()
  pass