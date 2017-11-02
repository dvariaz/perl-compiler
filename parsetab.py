
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftNOTleftLESSLESSEQUALGREATERGREATEREQUALISEQUALNOTEQUALleftLESS_STRINGLESSEQUAL_STRINGGREATER_STRINGGREATEREQUAL_STRINGISEQUAL_STRINGNOTEQUAL_STRINGleftPLUSMINUSleftTIMESDIVIDErightUMINUSPLUS MINUS TIMES MODULUS DIVIDE LESS LESSEQUAL GREATER GREATEREQUAL NOTEQUAL ISEQUAL COMP OR AND NOT ASSIGN PLUS_ASSIGN MINUS_ASSIGN MULTIPLY_ASSIGN DIVIDE_ASSIGN MOD_ASSIGN POW_ASSIGN DOLLAR AT PERCENT STRING INTEGER FLOAT HEX IF PRINT ELSE WHILE UNTIL FOR FOREACH LAST NEXT CONTINUE RETURN LESS_STRING GREATER_STRING LESSEQUAL_STRING GREATEREQUAL_STRING ISEQUAL_STRING NOTEQUAL_STRING COMP_STRING MY SUB USE PACKAGE GROSSARROW SEMICOLON COMMA LPAREN RPAREN LBRACKET RBRACKET LBLOCK RBLOCK AMPERSANT ID\n\tprogram : declaration_list\n\t\n\tdeclaration_list : declaration_list declaration\n\t\n\tdeclaration_list : declaration\n\t\n\tdeclaration : USE ID SEMICOLON\n                | PACKAGE ID SEMICOLON\n\t\n\tdeclaration : SUB ID LPAREN param_list RPAREN LBLOCK statement_list RBLOCK\n\t\n\tdeclaration : MY var_type SEMICOLON\n\t\t\t\t| MY var_type assign_type expression SEMICOLON\n\t\t\t\t| MY LPAREN param_list RPAREN SEMICOLON\n\t\t\t\t| MY LPAREN param_list RPAREN assign_type expression SEMICOLON\n\t\n\tparam_list : var_type comma_var_type\n\t\t\t   | empty\n\t\n\tcomma_var_type : comma_var_type COMMA var_type\n\t\t\t\t   | COMMA var_type\n\t\t\t\t   | empty\n\t\n\tvar_type : DOLLAR ID\n\t\t\t | AT ID\n\t\t\t | PERCENT ID\n\t\n\tassign_type : ASSIGN\n                | PLUS_ASSIGN\n                | MINUS_ASSIGN\n\t\t\t\t| MULTIPLY_ASSIGN\n\t\t\t\t| DIVIDE_ASSIGN\n\t\t\t\t| MOD_ASSIGN\n\t\t\t\t| POW_ASSIGN\n\t\n\tstatement_list : statement_list statement SEMICOLON\n\t\n\tstatement_list : statement SEMICOLON\n\t\n\tstatement_list : empty\n\t\n\tstatement : IF LPAREN relop RPAREN LBLOCK statement_list RBLOCK\n\t\n\tstatement : IF LPAREN relop RPAREN LBLOCK statement_list RBLOCK ELSE LBLOCK statement_list RBLOCK\n\t\n\tstatement : PRINT STRING\n\t\n\tstatement : WHILE LPAREN relop RPAREN LBLOCK statement_list RBLOCK\n\t\n\texpression_list : expression_listitems comma_expression\n\t\n\texpression_list : comma_expression\n\t\n\texpression_list : empty\n\t\n\texpression_listitems : expression_listitems comma_expression\n\t\n\texpression_listitems : expression\n\t\n\tcomma_expression : COMMA expression\n\t\n\texpression : expression PLUS expression\n\t\t\t   | expression MINUS expression\n\t\t\t   | expression TIMES expression\n\t\t\t   | expression DIVIDE expression\n\t\t\t   | expression MODULUS expression\n\t\n\texpression : INTEGER\n\t\t\t   | HEX\n\t\t\t   | FLOAT\n\t\t\t   | STRING\n\t\n\texpression : LPAREN expression RPAREN\n\t\n\texpression : ID LPAREN expression_list RPAREN %prec UMINUS\n\t\n\texpression : var_type\n\t\n\texpression : MINUS expression %prec UMINUS\n\t\n\texpression : PLUS expression %prec UMINUS\n\t\n\trelop : relop_number\n\t\t\t|\trelop_string\n\t\n\trelop_number :\tISEQUAL\n\t\t\t\t|\tNOTEQUAL\n\t\t\t\t|\tGREATER\n\t\t\t\t|\tGREATEREQUAL\n\t\t\t\t|\tLESS\n\t\t\t\t|\tLESSEQUAL\n\t\t\t\t|\tCOMP\n\t\n\trelop_string :\tISEQUAL_STRING\n\t\t\t\t|\tNOTEQUAL_STRING\n\t\t\t\t|\tGREATER_STRING\n\t\t\t\t|\tGREATEREQUAL_STRING\n\t\t\t\t|\tLESS_STRING\n\t\t\t\t|\tLESSEQUAL_STRING\n\t\t\t\t|\tCOMP_STRING\n\tempty :'
    
_lr_action_items = {'USE':([0,2,3,8,17,18,20,51,61,89,90,],[4,4,-3,-2,-4,-5,-7,-8,-9,-10,-6,]),'PACKAGE':([0,2,3,8,17,18,20,51,61,89,90,],[5,5,-3,-2,-4,-5,-7,-8,-9,-10,-6,]),'SUB':([0,2,3,8,17,18,20,51,61,89,90,],[6,6,-3,-2,-4,-5,-7,-8,-9,-10,-6,]),'MY':([0,2,3,8,17,18,20,51,61,89,90,],[7,7,-3,-2,-4,-5,-7,-8,-9,-10,-6,]),'$end':([1,2,3,8,17,18,20,51,61,89,90,],[0,-1,-3,-2,-4,-5,-7,-8,-9,-10,-6,]),'ID':([4,5,6,14,15,16,21,22,23,24,25,26,27,28,38,39,44,52,53,54,55,56,60,62,77,],[9,10,11,32,33,34,45,-19,-20,-21,-22,-23,-24,-25,45,45,45,45,45,45,45,45,45,45,45,]),'LPAREN':([7,11,21,22,23,24,25,26,27,28,38,39,44,45,52,53,54,55,56,60,62,77,83,85,],[13,19,44,-19,-20,-21,-22,-23,-24,-25,44,44,44,60,44,44,44,44,44,44,44,44,93,95,]),'DOLLAR':([7,13,19,21,22,23,24,25,26,27,28,38,39,44,48,52,53,54,55,56,60,62,63,77,],[14,14,14,14,-19,-20,-21,-22,-23,-24,-25,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'AT':([7,13,19,21,22,23,24,25,26,27,28,38,39,44,48,52,53,54,55,56,60,62,63,77,],[15,15,15,15,-19,-20,-21,-22,-23,-24,-25,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'PERCENT':([7,13,19,21,22,23,24,25,26,27,28,38,39,44,48,52,53,54,55,56,60,62,63,77,],[16,16,16,16,-19,-20,-21,-22,-23,-24,-25,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'SEMICOLON':([9,10,12,32,33,34,36,37,40,41,42,43,46,57,58,66,67,68,69,70,71,78,81,86,91,94,121,122,126,],[17,18,20,-16,-17,-18,-50,51,-44,-45,-46,-47,61,-52,-51,-39,-40,-41,-42,-43,-48,89,92,-49,96,-31,-29,-32,-30,]),'ASSIGN':([12,32,33,34,46,],[22,-16,-17,-18,22,]),'PLUS_ASSIGN':([12,32,33,34,46,],[23,-16,-17,-18,23,]),'MINUS_ASSIGN':([12,32,33,34,46,],[24,-16,-17,-18,24,]),'MULTIPLY_ASSIGN':([12,32,33,34,46,],[25,-16,-17,-18,25,]),'DIVIDE_ASSIGN':([12,32,33,34,46,],[26,-16,-17,-18,26,]),'MOD_ASSIGN':([12,32,33,34,46,],[27,-16,-17,-18,27,]),'POW_ASSIGN':([12,32,33,34,46,],[28,-16,-17,-18,28,]),'RPAREN':([13,19,29,30,31,32,33,34,35,36,40,41,42,43,47,49,57,58,59,60,64,66,67,68,69,70,71,72,74,75,79,86,87,88,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,],[-69,-69,46,-69,-12,-16,-17,-18,50,-50,-44,-45,-46,-47,-11,-15,-52,-51,71,-69,-14,-39,-40,-41,-42,-43,-48,86,-34,-35,-13,-49,-33,-38,115,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,116,]),'INTEGER':([21,22,23,24,25,26,27,28,38,39,44,52,53,54,55,56,60,62,77,],[40,-19,-20,-21,-22,-23,-24,-25,40,40,40,40,40,40,40,40,40,40,40,]),'HEX':([21,22,23,24,25,26,27,28,38,39,44,52,53,54,55,56,60,62,77,],[41,-19,-20,-21,-22,-23,-24,-25,41,41,41,41,41,41,41,41,41,41,41,]),'FLOAT':([21,22,23,24,25,26,27,28,38,39,44,52,53,54,55,56,60,62,77,],[42,-19,-20,-21,-22,-23,-24,-25,42,42,42,42,42,42,42,42,42,42,42,]),'STRING':([21,22,23,24,25,26,27,28,38,39,44,52,53,54,55,56,60,62,77,84,],[43,-19,-20,-21,-22,-23,-24,-25,43,43,43,43,43,43,43,43,43,43,43,94,]),'MINUS':([21,22,23,24,25,26,27,28,32,33,34,36,37,38,39,40,41,42,43,44,52,53,54,55,56,57,58,59,60,62,66,67,68,69,70,71,76,77,78,86,88,],[39,-19,-20,-21,-22,-23,-24,-25,-16,-17,-18,-50,53,39,39,-44,-45,-46,-47,39,39,39,39,39,39,-52,-51,53,39,39,-39,-40,-41,-42,53,-48,53,39,53,-49,53,]),'PLUS':([21,22,23,24,25,26,27,28,32,33,34,36,37,38,39,40,41,42,43,44,52,53,54,55,56,57,58,59,60,62,66,67,68,69,70,71,76,77,78,86,88,],[38,-19,-20,-21,-22,-23,-24,-25,-16,-17,-18,-50,52,38,38,-44,-45,-46,-47,38,38,38,38,38,38,-52,-51,52,38,38,-39,-40,-41,-42,52,-48,52,38,52,-49,52,]),'COMMA':([30,32,33,34,36,40,41,42,43,47,49,57,58,60,64,66,67,68,69,70,71,73,76,79,86,87,88,],[48,-16,-17,-18,-50,-44,-45,-46,-47,63,-15,-52,-51,77,-14,-39,-40,-41,-42,-43,-48,77,-37,-13,-49,-36,-38,]),'TIMES':([32,33,34,36,37,40,41,42,43,57,58,59,66,67,68,69,70,71,76,78,86,88,],[-16,-17,-18,-50,54,-44,-45,-46,-47,-52,-51,54,54,54,-41,-42,54,-48,54,54,-49,54,]),'DIVIDE':([32,33,34,36,37,40,41,42,43,57,58,59,66,67,68,69,70,71,76,78,86,88,],[-16,-17,-18,-50,55,-44,-45,-46,-47,-52,-51,55,55,55,-41,-42,55,-48,55,55,-49,55,]),'MODULUS':([32,33,34,36,37,40,41,42,43,57,58,59,66,67,68,69,70,71,76,78,86,88,],[-16,-17,-18,-50,56,-44,-45,-46,-47,-52,-51,56,-39,-40,-41,-42,56,-48,56,56,-49,56,]),'LBLOCK':([50,115,116,123,],[65,117,118,124,]),'IF':([65,80,82,92,96,117,118,119,120,124,125,],[83,83,-28,-27,-26,83,83,83,83,83,83,]),'PRINT':([65,80,82,92,96,117,118,119,120,124,125,],[84,84,-28,-27,-26,84,84,84,84,84,84,]),'WHILE':([65,80,82,92,96,117,118,119,120,124,125,],[85,85,-28,-27,-26,85,85,85,85,85,85,]),'RBLOCK':([65,80,82,92,96,117,118,119,120,124,125,],[-69,90,-28,-27,-26,-69,-69,121,122,-69,126,]),'ISEQUAL':([93,95,],[100,100,]),'NOTEQUAL':([93,95,],[101,101,]),'GREATER':([93,95,],[102,102,]),'GREATEREQUAL':([93,95,],[103,103,]),'LESS':([93,95,],[104,104,]),'LESSEQUAL':([93,95,],[105,105,]),'COMP':([93,95,],[106,106,]),'ISEQUAL_STRING':([93,95,],[107,107,]),'NOTEQUAL_STRING':([93,95,],[108,108,]),'GREATER_STRING':([93,95,],[109,109,]),'GREATEREQUAL_STRING':([93,95,],[110,110,]),'LESS_STRING':([93,95,],[111,111,]),'LESSEQUAL_STRING':([93,95,],[112,112,]),'COMP_STRING':([93,95,],[113,113,]),'ELSE':([121,],[123,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declaration_list':([0,],[2,]),'declaration':([0,2,],[3,8,]),'var_type':([7,13,19,21,38,39,44,48,52,53,54,55,56,60,62,63,77,],[12,30,30,36,36,36,36,64,36,36,36,36,36,36,36,79,36,]),'assign_type':([12,46,],[21,62,]),'param_list':([13,19,],[29,35,]),'empty':([13,19,30,60,65,117,118,124,],[31,31,49,75,82,82,82,82,]),'expression':([21,38,39,44,52,53,54,55,56,60,62,77,],[37,57,58,59,66,67,68,69,70,76,78,88,]),'comma_var_type':([30,],[47,]),'expression_list':([60,],[72,]),'expression_listitems':([60,],[73,]),'comma_expression':([60,73,],[74,87,]),'statement_list':([65,117,118,124,],[80,119,120,125,]),'statement':([65,80,117,118,119,120,124,125,],[81,91,81,81,91,91,81,91,]),'relop':([93,95,],[97,114,]),'relop_number':([93,95,],[98,98,]),'relop_string':([93,95,],[99,99,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> declaration_list','program',1,'p_program','perl_parser.py',23),
  ('declaration_list -> declaration_list declaration','declaration_list',2,'p_program_declaration_list','perl_parser.py',29),
  ('declaration_list -> declaration','declaration_list',1,'p_program_declaration','perl_parser.py',35),
  ('declaration -> USE ID SEMICOLON','declaration',3,'p_declaration_import','perl_parser.py',41),
  ('declaration -> PACKAGE ID SEMICOLON','declaration',3,'p_declaration_import','perl_parser.py',42),
  ('declaration -> SUB ID LPAREN param_list RPAREN LBLOCK statement_list RBLOCK','declaration',8,'p_declaration_function','perl_parser.py',48),
  ('declaration -> MY var_type SEMICOLON','declaration',3,'p_declaration_var','perl_parser.py',54),
  ('declaration -> MY var_type assign_type expression SEMICOLON','declaration',5,'p_declaration_var','perl_parser.py',55),
  ('declaration -> MY LPAREN param_list RPAREN SEMICOLON','declaration',5,'p_declaration_var','perl_parser.py',56),
  ('declaration -> MY LPAREN param_list RPAREN assign_type expression SEMICOLON','declaration',7,'p_declaration_var','perl_parser.py',57),
  ('param_list -> var_type comma_var_type','param_list',2,'p_param_list','perl_parser.py',63),
  ('param_list -> empty','param_list',1,'p_param_list','perl_parser.py',64),
  ('comma_var_type -> comma_var_type COMMA var_type','comma_var_type',3,'p_comma_var_type','perl_parser.py',70),
  ('comma_var_type -> COMMA var_type','comma_var_type',2,'p_comma_var_type','perl_parser.py',71),
  ('comma_var_type -> empty','comma_var_type',1,'p_comma_var_type','perl_parser.py',72),
  ('var_type -> DOLLAR ID','var_type',2,'p_var_type','perl_parser.py',77),
  ('var_type -> AT ID','var_type',2,'p_var_type','perl_parser.py',78),
  ('var_type -> PERCENT ID','var_type',2,'p_var_type','perl_parser.py',79),
  ('assign_type -> ASSIGN','assign_type',1,'p_assign_type','perl_parser.py',85),
  ('assign_type -> PLUS_ASSIGN','assign_type',1,'p_assign_type','perl_parser.py',86),
  ('assign_type -> MINUS_ASSIGN','assign_type',1,'p_assign_type','perl_parser.py',87),
  ('assign_type -> MULTIPLY_ASSIGN','assign_type',1,'p_assign_type','perl_parser.py',88),
  ('assign_type -> DIVIDE_ASSIGN','assign_type',1,'p_assign_type','perl_parser.py',89),
  ('assign_type -> MOD_ASSIGN','assign_type',1,'p_assign_type','perl_parser.py',90),
  ('assign_type -> POW_ASSIGN','assign_type',1,'p_assign_type','perl_parser.py',91),
  ('statement_list -> statement_list statement SEMICOLON','statement_list',3,'p_statement_list','perl_parser.py',97),
  ('statement_list -> statement SEMICOLON','statement_list',2,'p_statement_list_statement','perl_parser.py',103),
  ('statement_list -> empty','statement_list',1,'p_statement_list_empty','perl_parser.py',109),
  ('statement -> IF LPAREN relop RPAREN LBLOCK statement_list RBLOCK','statement',7,'p_statement_if','perl_parser.py',115),
  ('statement -> IF LPAREN relop RPAREN LBLOCK statement_list RBLOCK ELSE LBLOCK statement_list RBLOCK','statement',11,'p_statement_if_else','perl_parser.py',121),
  ('statement -> PRINT STRING','statement',2,'p_statement_print','perl_parser.py',127),
  ('statement -> WHILE LPAREN relop RPAREN LBLOCK statement_list RBLOCK','statement',7,'p_statement_while','perl_parser.py',133),
  ('expression_list -> expression_listitems comma_expression','expression_list',2,'p_expression_list','perl_parser.py',139),
  ('expression_list -> comma_expression','expression_list',1,'p_expression_list_comma_expression','perl_parser.py',145),
  ('expression_list -> empty','expression_list',1,'p_expression_list_empty','perl_parser.py',151),
  ('expression_listitems -> expression_listitems comma_expression','expression_listitems',2,'p_expression_listitems','perl_parser.py',157),
  ('expression_listitems -> expression','expression_listitems',1,'p_expression_listitems_expr','perl_parser.py',163),
  ('comma_expression -> COMMA expression','comma_expression',2,'p_comma_expression','perl_parser.py',169),
  ('expression -> expression PLUS expression','expression',3,'p_expression','perl_parser.py',175),
  ('expression -> expression MINUS expression','expression',3,'p_expression','perl_parser.py',176),
  ('expression -> expression TIMES expression','expression',3,'p_expression','perl_parser.py',177),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','perl_parser.py',178),
  ('expression -> expression MODULUS expression','expression',3,'p_expression','perl_parser.py',179),
  ('expression -> INTEGER','expression',1,'p_datatype_expression','perl_parser.py',185),
  ('expression -> HEX','expression',1,'p_datatype_expression','perl_parser.py',186),
  ('expression -> FLOAT','expression',1,'p_datatype_expression','perl_parser.py',187),
  ('expression -> STRING','expression',1,'p_datatype_expression','perl_parser.py',188),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_on_paren_expression','perl_parser.py',194),
  ('expression -> ID LPAREN expression_list RPAREN','expression',4,'p_call_expression','perl_parser.py',200),
  ('expression -> var_type','expression',1,'p_var_type_expression','perl_parser.py',205),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus_minus','perl_parser.py',210),
  ('expression -> PLUS expression','expression',2,'p_expression_uminus_plus','perl_parser.py',216),
  ('relop -> relop_number','relop',1,'p_relop','perl_parser.py',222),
  ('relop -> relop_string','relop',1,'p_relop','perl_parser.py',223),
  ('relop_number -> ISEQUAL','relop_number',1,'p_relop_number','perl_parser.py',229),
  ('relop_number -> NOTEQUAL','relop_number',1,'p_relop_number','perl_parser.py',230),
  ('relop_number -> GREATER','relop_number',1,'p_relop_number','perl_parser.py',231),
  ('relop_number -> GREATEREQUAL','relop_number',1,'p_relop_number','perl_parser.py',232),
  ('relop_number -> LESS','relop_number',1,'p_relop_number','perl_parser.py',233),
  ('relop_number -> LESSEQUAL','relop_number',1,'p_relop_number','perl_parser.py',234),
  ('relop_number -> COMP','relop_number',1,'p_relop_number','perl_parser.py',235),
  ('relop_string -> ISEQUAL_STRING','relop_string',1,'p_relop_string','perl_parser.py',241),
  ('relop_string -> NOTEQUAL_STRING','relop_string',1,'p_relop_string','perl_parser.py',242),
  ('relop_string -> GREATER_STRING','relop_string',1,'p_relop_string','perl_parser.py',243),
  ('relop_string -> GREATEREQUAL_STRING','relop_string',1,'p_relop_string','perl_parser.py',244),
  ('relop_string -> LESS_STRING','relop_string',1,'p_relop_string','perl_parser.py',245),
  ('relop_string -> LESSEQUAL_STRING','relop_string',1,'p_relop_string','perl_parser.py',246),
  ('relop_string -> COMP_STRING','relop_string',1,'p_relop_string','perl_parser.py',247),
  ('empty -> <empty>','empty',0,'p_empty','perl_parser.py',252),
]