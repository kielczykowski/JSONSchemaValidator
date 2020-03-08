#!/usr/bin/python3
import re as regex
import collections
import json
import sys

Token = collections.namedtuple("Token", ["type", "value", "line", "collumn"])

class Scanner:

  def __init__ (self, input_string):
    print("Starting scanner")
    self.tokens_ = []
    self.current_token_ = 0
    for token in self.tokenize(input_string):
      self.tokens_.append(token)
    with open("TEST.txt",'w') as file:
      for token in self.tokens_:
        file.write(str(token))
        file.write("\n")

  def tokenize(self, input_string):
    types = self.readTypeSpecs()
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
    while match is not None:
      type = match.lastgroup
      if type == 'NEWLINE':
        line_start = current_position
        line_number += 1
      elif type != 'SKIP':
        value = match.group(type).strip("\"")
        print(value.upper())
        if type == 'STRING':
          yield Token("QUOT", "\"", line_number, match.start()-line_start)
          if value in keywords:
            type = value.upper()
          if value in types.keys():
            type = types[value]
          yield Token(type, value, line_number, match.start()-line_start+1)
          yield Token("QUOT", "\"", line_number, match.end()-(line_start+1))
        else:
          yield Token(type, value, line_number, match.start()-line_start)
      current_position = match.end()
      match = get_token(input_string, current_position)
    if current_position != len(input_string):
      raise RuntimeError('Error: Unexpected character %r on line %d' % \
                              (input_string[current_position], line_number))
    yield Token('EOF', '', line_number, current_position-line_start)

  def readKeywords(self):
    with open("keywords") as kw:
      return [word.strip(" \t\n") for word in kw.read().split(sep=",")]

  def readTokenSpecs(self):
    with open("token_specs") as token_specs:
      return [(spec.split("::")[0], spec.split("::")[1].strip(" \t\n")) for spec in token_specs.readlines()]
  
  def readTypeSpecs(self):
    data = {}
    with open("type_specs") as type_specs:
      data = json.load(type_specs)
      return data["types"]
    # for key, value  in data["types"].items():
    #   print(key, value)

  
  def nextToken(self):
    # TODO get next token
    pass

if __name__ == "__main__":
  scanner = Scanner(sys.argv[1])
  pass