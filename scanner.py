#!/usr/bin/python3
import re as regex
import collections
import sys

Token = collections.namedtuple("Token", ["type", "value", "line", "collumn"])

class Scanner:

  def __init__ (self, input_string):
    print("Starting scanner")
    self.tokens_ = []
    self.current_token_ = 0
    self.tokens = self.tokenize(input_string)

  def tokenize(self, input_string):
    keywords = self.readKeywords()
    token_specs = self.readTokenSpecs()
    token_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specs)
    get_token = regex.compile(token_regex).match
    line_number = 1
    current_position = line_start = 0
    match = get_token(input_string)
    print ('token_regex')
    print (token_regex)
    print('keywords')
    print(keywords)
    print('token_specs')
    print(token_specs)
    # TODO logic of scanner

    # TODO return list of tokens
    return 0 

  def readKeywords(self):
    with open("keywords") as kw:
      return [word.upper().strip(" \t\n") for word in kw.read().split(sep=",")]

  def readTokenSpecs(self):
    with open("token_specs") as token_specs:
      return [(spec.split(",")[0], spec.split(",")[1].strip(" \t\n")) for spec in token_specs.readlines()]

  
  def nextToken(self):
    # TODO get next token
    pass

if __name__ == "__main__":
  scanner = Scanner(sys.argv[1])
  pass