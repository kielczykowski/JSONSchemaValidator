import scanner

class Parser:
  ##### Parser header ######
  def __init__(self, tokenizer):
    self.nextToken = tokenizer.nextToken
    self.token = self.nextToken()

  def takeToken(self, token_type):
    if self.token.type != token_type :
      self.error("Unexpected token: {}, got {}".format(token_type, self.token.type))
    if token_type != 'EOF':
      self.token = self.nextToken()

  def error (self, msg):
    raise RuntimeError('Parser Error, {}'.format(msg))
  
  ##### Parser body ######

  def start(self):
    # start -> OCB program CCB EOF
    self.takeToken("OCB")
    self.program()
    self.takeToken("CCB")
    self.takeToken("EOF") 
  
  def program(self):
    # program -> start_statement program
    if self.token.type == "QUOT":
      self.start_statement()
      self.program()
    else:
      pass
  
  def start_statement(self):
    self.takeToken("QUOT")
    # if self.token.type == "$ID" or self.token.type == "$SCHEMA" or self.token.type == "TITLE" or self.token.type == "TYPE" or \
    #    self.token.type == "PROPERTIES" or self.token.type == "DESCRIPTION" or self.token.type == "REQUIRED" or self.token.type == "MINIMUM" or \
    #    self.token.type == "MAXIMUM" or self.token.type == "MINLENGTH" or self.token.type == "MAXLENGTH" or self.token.type == "ENUM" or \
    #    self.token.type == "DEFINITIONS" or self.token.type == "$REF":
    self.statement()
    self.statement_continuation()
    # else:
    #   self.error("Epsilon not allowed")
    
  def statement_continuation(self):
    if self.token.type == "COMMA":
      self.takeToken("COMMA")
      self.takeToken("QUOT")
      self.statement()
      self.statement_continuation()
    else:
      pass

    
  def statement(self):
    if self.token.type == "$ID":
      self.id_stmt()
    elif self.token.type == "$SCHEMA":
      self.schema_stmt()
    elif self.token.type == "TITLE" or self.token.type == "DESCRIPTION":
      self.specification_stmt()
    elif self.token.type == "TYPE":
      self.type_stmt()
    elif self.token.type == "PROPERTIES":
      self.property_stmt()
    elif self.token.type == "REQUIRED":
      self.required_stmt()
    elif self.token.type == "MINIMUM" or self.token.type == "MAXIMUM" or \
         self.token.type == "MINLENGTH" or self.token.type == "MAXLENGTH":
      self.boundary_stmt()
    elif self.token.type == "ENUM":
      self.enum_stmt()
    elif self.token.type == "DEFINITIONS":
      self.definition_stmt()
    elif self.token.type == "$REF":
      self.ref_stmt()
    elif self.token.type == "STRING":
      self.regular_stmt()
    else:
      self.error("Epsilon not allowed")
  
  def id_stmt(self):
      self.takeToken("$ID")
      self.qcq_stmt_separator()
      self.takeToken("STRING")
      self.takeToken("QUOT")
      print("id_stmt: OK")
  
  def schema_stmt(self):
      self.takeToken("$SCHEMA")
      self.qcq_stmt_separator()
      self.takeToken("STRING")
      self.takeToken("QUOT")
      print("schema_stmt: OK")
    
  def specification_stmt(self):
    if self.token.type == "TITLE":
      self.title_stmt()
    elif self.token.type == "DESCRIPTION":
      self.description_stmt()
    else:
      self.error("Epsilon not allowed")
    
  def title_stmt(self):
    self.takeToken("TITLE")
    self.qcq_stmt_separator()
    self.takeToken("STRING")
    self.takeToken("QUOT")
    print("title_stmt: OK")
  
  def description_stmt(self):
    self.takeToken("DESCRIPTION")
    self.qcq_stmt_separator()
    self.takeToken("STRING")
    self.takeToken("QUOT")
    print("description_stmt: OK")
  
  def required_stmt(self):
    self.takeToken("REQUIRED")
    self.qc_stmt_separator()
    self.string_array()
    print("required_stmt: OK")
  
  def type_stmt(self):
    self.takeToken("TYPE")
    self.qc_stmt_separator()
    self.type_element()
    print("type_stmt: OK")
  
  def boundary_stmt(self):
    if  self.token.type == "MINIMUM" or self.token.type == "MAXIMUM":
      self.number_boundary_stmt()
    elif self.token.type == "MINLENGTH" or self.token.type == "MAXLENGTH":
      self.str_len_boundary_stmt()
    else:
      self.error("boundary_stmt not found, got {}".format(self.token.type))
    


  def number_boundary_stmt(self):
    self.min_max()
    self.qc_stmt_separator()
    if self.token.type == "SIGN":
      self.takeToken("SIGN")
    self.number()
    print("number_boundary_stmt: OK")
  
  def str_len_boundary_stmt(self):
    self.min_max_len()
    self.qc_stmt_separator()
    self.takeToken("INTEGER")
    print("str_len_boundary_stmt: OK")
  
  def enum_stmt(self):
    self.takeToken("ENUM")
    self.qc_stmt_separator()
    self.any_type_array()
    print("enum_stmt: OK")
  
  def regular_stmt(self):
    self.takeToken("STRING")
    self.qc_stmt_separator()
    if self.token.type == "SIGN" or self.token.type == "QUOT" or self.token.type == "INTEGER" or self.token.type == "NUMBER":
      self.value()
    elif self.token.type == "OSB":
      self.any_type_array()
    elif self.token.type == " OCB":
      self.object()
    else :
      self.error("Expected regular_stmt, got {}".format(self.token.type))
    print("regular_stmt: OK")

  def property_stmt(self):
    self.takeToken("PROPERTIES")
    self.qc_stmt_separator()
    self.hash()
    print("property_stmt: OK")

  def definition_stmt(self):
    self.takeToken("DEFINITIONS")
    self.qc_stmt_separator()
    self.hash()
    print("definition_stmt: OK")
  
  def ref_stmt(self):
    self.takeToken("$REF")
    self.qcq_stmt_separator()
    self.takeToken("REF_URI")
    self.takeToken("QUOT")
    print("ref_stmt: OK")
    
  def hash(self):
    self.takeToken("OCB")
    self.string()
    self.takeToken("COLON")
    self.object()
    self.hash_continuation()
    self.takeToken("CCB")

  def hash_continuation(self):
    if self.token.type == "COMMA":
      self.takeToken("COMMA")
      self.string()
      self.takeToken("COLON")
      self.object()
      self.hash_continuation()
    else:
      pass

  def object(self):
    self.takeToken("OCB")
    if self.token.type == "QUOT":
      self.program()
    self.takeToken("CCB")
  
  def any_type_array(self):
    self.takeToken("OSB")
    if self.token.type == "SIGN" or self.token.type == "QUOT" or self.token.type == "INTEGER" or self.token.type == "NUMBER":
      self.any_type_element()
      self.any_type_table_continuation()
    self.takeToken("CSB")
  
  def any_type_element(self):
    if self.token.type == "SIGN":
      self.takeToken("SIGN")
      self.number()
    elif self.token.type == "INTEGER" or self.token.type == "NUMBER":
      self.number()
    elif self.token.type == "QUOT":
      self.string()
    else:
      self.error("Expected any_type_element, got {}".format(self.token.type))
    
  def any_type_table_continuation(self):
    if self.token.type == "COMMA":
      self.takeToken("COMMA")
      self.any_type_element()
      self.any_type_table_continuation()
    else:
      pass

  def qcq_stmt_separator(self):
    self.takeToken("QUOT")
    self.takeToken("COLON")
    self.takeToken("QUOT")
  
  def qc_stmt_separator(self):
    self.takeToken("QUOT")
    self.takeToken("COLON")

  def string_array (self):
    self.takeToken("OSB")
    if self.token.type == "QUOT":
      self.string()
      self.string_array_continuation()
    self.takeToken("CSB")
  
  def string_array_continuation(self):
    if self.token.type == "COMMA":
      self.takeToken("COMMA")
      self.string()
      self.string_array_continuation()
    else:
      pass

  def string(self):
    self.takeToken("QUOT")
    
    if self.token.type == "$ID" or self.token.type == "$SCHEMA" or self.token.type == "TITLE" or self.token.type == "TYPE" or \
       self.token.type == "PROPERTIES" or self.token.type == "DESCRIPTION" or self.token.type == "REQUIRED" or self.token.type == "MINIMUM" or \
       self.token.type == "MAXIMUM" or self.token.type == "MINLENGTH" or self.token.type == "MAXLENGTH" or self.token.type == "ENUM" or \
       self.token.type == "DEFINITIONS" or self.token.type == "$REF":
      self.keyword()
    elif self.token.type == "STRING":
      self.takeToken("STRING")
    elif self.token.type == "ARR_TYPE" or self.token.type == "BOOL_TYPE" or self.token.type == "OBJ_TYPE" or \
         self.token.type == "NULL_TYPE" or self.token.type == "NUM_TYPE" or self.token.type == "INT_TYPE" or \
         self.token.type == "STR_TYPE":
      self.type()
    
    self.takeToken("QUOT")
  
  def type_element(self):
    if self.token.type == "QUOT":
      self.type_string()
    elif self.token.type == "OSB":
      self.type_array()
    else:
      self.error("type_element not found, got {}".format(self.token.type))
    
  def type_array(self):
    self.takeToken("OSB")
    self.type_string()
    self.type_array_continuation()
    self.takeToken("CSB")
  
  def type_array_continuation(self):
    if self.token.type == "COMMA":
      self.takeToken("COMMA")
      self.type_string()
      self.type_array_continuation()
    else:
      pass
  
  def type_string(self):
    self.takeToken("QUOT")
    self.type()
    self.takeToken("QUOT")
  
  def type(self):
    if self.token.type == "ARR_TYPE":
      self.takeToken("ARR_TYPE")
    elif self.token.type == "BOOL_TYPE":
      self.takeToken("BOOL_TYPE")
    elif self.token.type == "OBJ_TYPE":
      self.takeToken("OBJ_TYPE")
    elif self.token.type == "NULL_TYPE":
      self.takeToken("NULL_TYPE")
    elif self.token.type == "NUM_TYPE":
      self.takeToken("NUM_TYPE")
    elif self.token.type == "INT_TYPE":
      self.takeToken("INT_TYPE")
    elif self.token.type == "STR_TYPE":
      self.takeToken("STR_TYPE")
    else :
      self.error("Expected type not found, got {}".format(self.token.type))
  
  def number(self):
    if self.token.type == "NUMBER":
      self.takeToken("NUMBER")
    elif self.token.type == "INTEGER":
      self.takeToken("INTEGER")
    else:
      self.error("Expected number,  got {}".format(self.token.type))

  def value(self):
    if self.token.type == "SIGN":
      self.takeToken("SIGN")
      self.number()
    elif self.token.type == "INTEGER" or self.token.type == "NUMBER":
      self.number()
    elif self.token.type == "QUOT":
      self.string()
    else:
      self.error("Expected any_type_element, got {}".format(self.token.type))

  def keyword(self):
    if self.token.type == "$ID":
      self.takeToken("$ID")
    elif self.token.type == "$SCHEMA":
      self.takeToken("$SCHEMA")
    elif self.token.type == "TITLE":
      self.takeToken("TITLE")
    elif self.token.type == "TYPE":
      self.takeToken("TYPE")
    elif self.token.type == "PROPERTIES":
      self.takeToken("PROPERTIES")
    elif self.token.type == "DESCRIPTION":
      self.takeToken("DESCRIPTION")
    elif self.token.type == "REQUIRED":
      self.takeToken("REQUIRED")
    elif self.token.type == "MINIMUM" or self.token.type == "MAXIMUM" :
      self.min_max()
    elif self.token.type == "MINLENGTH" or self.token.type == "MAXLENGTH":
      self.min_max_len()
    elif self.token.type == "ENUM":
      self.takeToken("ENUM")
    elif self.token.type == "DEFINITIONS":
      self.takeToken("DEFINITIONS")
    elif self.token.type == "$REF":
      self.takeToken("$REF")
    else:
      self.error("Expected keyword not found, got {}".format(self.token.type))
    
  
  def min_max(self):
    if self.token.type == "MINIMUM":
      self.takeToken("MINIMUM")
    elif self.token.type == "MAXIMUM":
      self.takeToken("MAXIMUM")
    else:
      self.error("Epsilon not allowed, min_max not found")

  def min_max_len(self):
    if self.token.type == "MINLENGTH":
      self.takeToken("MINLENGTH")
    elif self.token.type == "MAXLENGTH":
      self.takeToken("MAXLENGTH")
    else :
      self.error("Epsilon not allowed, min_max not found")
    
      



if __name__ == "__main__":
  pass 
