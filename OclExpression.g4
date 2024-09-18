grammar OclExpression;

oclExp:
    primaryExp                                # PrimaryExpression
|   unrestrictedName                                      # SimpleName
|   (unrestrictedName '::')+ unreservedName               # FullQualifiedName
|   expression=oclExp argExp                               # CallExpression
|   expression=oclExp '.' attname=unrestrictedName  argExp        # MethodCall
|   expression=oclExp '.' attname=unrestrictedName             # AttributeNavigation
|   expression=oclExp '->' attname=unrestrictedName argExp     # CollectionCall
|   operator='-' expression=oclExp                    # UnaryOperation
|   operator='not' expression=oclExp                  # UnaryOperation
|   left=oclExp operator='*' right=oclExp         # ArithmeticBinaryOperation
|   left=oclExp operator='/' right=oclExp         # ArithmeticBinaryOperation
|   left=oclExp operator='+' right=oclExp         # ArithmeticBinaryOperation
|   left=oclExp operator='-' right=oclExp         # ArithmeticBinaryOperation
|   left=oclExp operator='<' right=oclExp         # ComparisonBinaryOperation
|   left=oclExp operator='>' right=oclExp         # ComparisonBinaryOperation
|   left=oclExp operator='<=' right=oclExp        # ComparisonBinaryOperation
|   left=oclExp operator='>=' right=oclExp        # ComparisonBinaryOperation
|   left=oclExp operator='=' right=oclExp         # ComparisonBinaryOperation
|   left=oclExp operator='<>' right=oclExp         # ComparisonBinaryOperation
|   left=oclExp operator='and' right=oclExp       # BooleanBinaryOperation
|   left=oclExp operator='or' right=oclExp        # BooleanBinaryOperation
|   left=oclExp operator='xor' right=oclExp       # BooleanBinaryOperation
|   left=oclExp operator='implies' right=oclExp   # BooleanBinaryOperation
;

argExp:
    '(' (body+=oclExp (',' body+=oclExp)*)? ')'           # ArgumentsExp
|   '(' varnames+=unreservedName (',' varnames+=unreservedName )* (':' typeExpCS)? ('=' initializer=oclExp)? '|' body=oclExp ')'      # LambdaExp
;

primaryExp:
		selfExp
|		nestedExp
|		primitiveLiteralExp
|		tupleLiteralExp
|		collectionLiteralExp
|		typeLiteralExp
|		letExp
|		ifExp
;

selfExp:
    'self'
;

nestedExp:
    '(' nested=oclExp ')'
;

primitiveLiteralExp:
	    numberLiteralExpCS          # NumberLiteral
|	    booleanLiteralExpCS         # BooleanLiteral
|	    stringLiteralExpCS          # StringLiteral
|	    unlimitedNaturalLiteralCS   # UnlimitedNaturalLiteral
|	    invalidLiteralExpCS         # InvalidLiteral
|	    nullLiteralExpCS            # NullLiteral
;

tupleLiteralExp:
    'Tuple' '{' tupleLiteralPartCS (',' tupleLiteralPartCS)*'}'
;

tupleLiteralPartCS:
    unrestrictedName (':' typeExpCS)? '=' primaryExp
;

collectionLiteralExp:
    collectionTypeCS '{' (expressions+=collectionLiteralPartCS (',' expressions+=collectionLiteralPartCS)*)? '}'
;

collectionTypeCS:
    collectionTypeIdentifier ('(' typeExpCS ')'|'<' typeExpCS '>')?
;

primitiveTypeCS:
    'String'            # StringType
|   'Integer'           # IntegerType
|   'UnlimitedNatural'  # UnlimitedNaturalType
|   'Boolean'           # BooleanType
;

collectionTypeIdentifier:
    'Collection'    # CollectionType
|   'Bag'           # BagType
|   'OrderedSet'    # OrderedSetType
|   'Sequence'      # SequenceType
|   'Set'           # SetType
;

collectionLiteralPartCS:
    oclExp
|   inf=oclExp isInterval='..' sup=oclExp
;

typeLiteralExp:
    typeLiteralCS
;

letExp:
    'let' variables+=letVariableCS (',' variables+=letVariableCS)* 'in' oclExp
;

letVariableCS:
    unrestrictedName (':' typeExpCS)? '=' oclExp
;

typeExpCS:
    typeLiteralCS
|   typeNameExpCS
;

typeNameExpCS:
    unrestrictedName
|   typeNameExpCS ('::' unreservedName)+
;

typeLiteralCS:
    collectionTypeCS
|   primitiveTypeCS
|   tupleTypeCS
;

tupleTypeCS:
    'Tuple' ('(' tuplePartCS (',' tuplePartCS)* ')'
|   '<' tuplePartCS (',' tuplePartCS)* '>')?
;

tuplePartCS:
    unrestrictedName ':' typeExpCS
;

ifExp:
    'if' condition=oclExp 'then' body=oclExp 'else' else_=oclExp 'endif'
;

numberLiteralExpCS:
    INT
|   FLOAT
;

stringLiteralExpCS:
    STRING
;

booleanLiteralExpCS:
    'true'|'false'
;

unlimitedNaturalLiteralCS:
    '*'
;

invalidLiteralExpCS:
    'invalid'
;

nullLiteralExpCS:
    'null'
;

unrestrictedName: ~('('|')'|'true'|'false'|'and'|'else'|'endif'|'false'|'if'|'implies'|'in'|'invalid'|'let'|'not'|'null'|'or'|'self'|'then'|'true'|'xor'|'Bag'|'Boolean'|'Collection'|'Integer'|'Lambda'|'OclAny'|'OclInvalid'|'OclMessage'|'OclSelf'|'OclVoid'|'OrderedSet'|'Real'|'Sequence'|'Set'|'String'|'Tuple'|'UnlimitedNatural');
unreservedName: ~('('|')'|'and'|'else'|'endif'|'false'|'if'|'implies'|'in'|'invalid'|'let'|'not'|'null'|'or'|'self'|'then'|'true'|'xor');

STRING: '\'' ~[']* '\'';
SPECIAL_VARNAME: '_' STRING;
VARNAME: [a-zA-Z_][a-zA-Z_0-9]*;
INT: [0-9]+;
FLOAT:  INT ('.' INT)? (('e'|'E') ('+'|'-')? INT)?;

// COMMENT:LINE_COMMENT|BLOCK_COMMENT|DOCU_COMMENT;
// LINE_COMMENT:'--' .*? '\n';
// BLOCK_COMMENT: '/*' .*? '*/';
// DOCU_COMMENT: '/**' .*? '*/';
WS: [ \n\t\r]+ -> skip;
