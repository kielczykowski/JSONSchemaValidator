# Json Schema Validator

## Description

This project is part of student project. The main goal is to implement programe responsible for validating Json Schema.

***Project might not implement all features defined in JSON Schema documentation.***

## Running project

To run current state of project type:

```
./validator.py exampleFile.txt
```

or

```
python3 validator.py exampleFile.txt
```

Running script needs path to input file as command line argument.

## Details

Project will be created based on BNF notation.

Json Schema attributes to implement:
  - : -> COLON
  - { -> OCB
  - } -> CCB
  - $schema -> SCHEMA
  - $id -> IDENTIFIER
  - $ref -> REF
  - title -> TITLE
  - type -> TYPE
  - properties -> PROPS
  - description -> DESC
  - required -> REQ
  - minimum -> MIN
  - maximum -> MAX
  - minLength-> MINLEN
  - maxLength -> MAXLEN
  - enum -> ENUM
  - definitions -> DEF