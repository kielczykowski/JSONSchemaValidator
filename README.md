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

| Symbol        | Expression        |
|---------------|:------------------|
| start | OCB program CCB EOF|
| program | start_statement program        |
|         | eps                            |
| start_statement | QUOT statement statement_continuation program |
| statement_continuation  | COMMA QUOT statement statement_continuation  |
|                         | eps                           |
| statement | id_stmt       |
|           | schema_stmt   |
|           | specification_stmt    |
|           | required_stmt |
|           | type_stmt     |
|           | boundary_stmt |
|           | enum_stmt     |
|           | regular_stmt  |
|           | property_stmt |
|           | definition_stmt |
| **TODO**  | ref_stmt     |
| **TODO**  | REF_URI    |
|  id_stmt  |   $ID qcq_stmt_separator STRING QUOT |
| schema_stmt | $SCHEMA qcq_stmt_separator STRING QUOT  |
| specification_stmt  | title_stmt  |
|                     | description_stmt  |
| title_stmt |  TITLE qcq_stmt_separator STRING QUOT |
| description_stmt |  DESCRIPTION qcq_stmt_separator STRING QUOT|
| required_stmt | REQUIRED qc_stmt_separator string_array  |
| type_stmt | TYPE qc_stmt_separator type_element |
| boundary_stmt | number_boundary_stmt   |
|               | str_len_boundary_stmt  | 
| enum_stmt | ENUM qc_stmt_separator any_type_array  |
| number_boundary_stmt  | min_max qc_stmt_separator SIGN number |
|                       | min_max qc_stmt_separator number |
| str_len_boundary_stmt | min_max_len qc_stmt_separator INTEGER  |
| regular_stmt  | STRING qc_stmt_separator value           |
|               | STRING qc_stmt_separator any_type_array  |
|               | STRING qc_stmt_separator object          |
| property_stmt | PROPERTIES qc_stmt_separator hash  |
| definition_stmt | DEFINITIONS qc_stmt_separator hash |
| ref_stmt  | $REF qcq_stmt_separator REF_URI QUOT  |
| qcq_stmt_separator  | QUOT COLON QUOT |
| qc_stmt_separator | QUOT COLON  |
| hash |  OCB string COLON object hash_continuation CCB |
| hash_continuation | COMMA string COLON object hash_continuation |
|                   | eps                                         |
| object  | OCB program CCB |
|         | OCB CCB         |
| any_type_array  | OSB any_type_element any_type_table_continuation CSB  |
|                 | OSB CSB                                               |
| any_type_table_continuation | COMMA any_type_element  any_type_table_continuation |
|                             | eps                                                 |
| any_type_element  | SIGN number           |
|                   | number                |
|                   | string |
| string_array  | OSB string  string_array_continuation CSB|
|               | OSB CSB|
| string_array_continuation | COMMA string string_array_continuation |
|                           | eps                                                  |
| type_element |  type_string |
|              |  type_array  |
| type_array  | OSB type_string type_array_continuation CSB |
| type_array_continuation | COMMA type_string type_array_continuation |
|                         | eps                                       |
| type_string | QUOT type QUOT | 
| type  | ARR_TYPE  |
|       | BOOL_TYPE |
|       | OBJ_TYPE  |
|       | NULL_TYPE |
|       | NUM_TYPE  |
|       | INT_TYPE  |
|       | STR_TYPE  |
| number  | NUMBER  |
|         | INTEGER |
| keyword | $ID         |
|         | $SCHEMA     |
|         | TITLE       | 
|         | TYPE        |
|         | PROPERTIES  |
|         | DESCRIPTION |
|         | REQUIRED    | 
|         | min_max     |
|         | min_max_len |
|         | ENUM        |
|         | DEFINITIONS | 
|         | $REF        |
| min_max | MINIMUM |
|         | MAXIMUM |
| min_max_len | MINLENGTH |
|             | MAXLENGTH |
| value | SIGN number           |
|       | number                |
|       | string                |
| string  | QUOT STRING QUOT  | 
|         | QUOT keyword QUOT |
|         | QUOT type QUOT    |
|         | QUOT  QUOT        |





