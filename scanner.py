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
    for token in self.tokenize(input_string):
      self.tokens_.append(token)
    for token in self.tokens_:
      print(token)

  def tokenize(self, input_string):
    keywords = self.readKeywords()
    token_specs = self.readTokenSpecs()
    token_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specs)
    get_token = regex.compile(token_regex).match
    line_number = 1
    current_position = line_start = 0
    match = get_token(input_string)
    # print(input_string)
    print ('token_regex')
    print (token_regex)
    print('keywords')
    print(keywords)
    # print('token_specs')
    # print(token_specs)
    # TODO logic of scanner
    while match is not None:
      type = match.lastgroup
      # print(match)
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
          yield Token(type, value, line_number, match.start()-line_start+1)
          yield Token("QUOT", "\"", line_number, match.end()-(line_start+1))
        else:
          yield Token(type, value, line_number, match.start()-line_start)
      # print(type)
      current_position = match.end()
      match = get_token(input_string, current_position)
      # print(current_position)
      # print(len(input_string))
      # yield Token(type, "XD", line_number, match.start()-line_start)
    if current_position != len(input_string):
      raise RuntimeError('Error: Unexpected character %r on line %d' % \
                              (input_string[current_position], line_number))
    yield Token('EOF', '', line_number, current_position-line_start)


    # TODO return list of tokens
    # return 0 

  def readKeywords(self):
    with open("keywords") as kw:
      return [word.strip(" \t\n") for word in kw.read().split(sep=",")]

  def readTokenSpecs(self):
    with open("token_specs") as token_specs:
      return [(spec.split("::")[0], spec.split("::")[1].strip(" \t\n")) for spec in token_specs.readlines()]

  
  def nextToken(self):
    # TODO get next token
    pass

if __name__ == "__main__":
  scanner = Scanner(sys.argv[1])
  pass