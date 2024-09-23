grammar OclExpression;

@parser::header {
OBJ = object
CANNOT_EVAL = object()  # define a sentinel object

def has_result(*args):
    return all(e.r is not None and e.r is not CANNOT_EVAL for e in args)

def f(vs, ts, eval):
    for v, t in zip(vs, ts):
        if v is CANNOT_EVAL or not isinstance(v, t):
            return CANNOT_EVAL
    return eval(*vs)
}

oclExp
	returns[r]:
	n = primaryExp {$r = $n.r}										                    # PrimaryExpression
	| unrestrictedName	{$r = CANNOT_EVAL}							                    # SimpleName
	| (unrestrictedName '::')+ unreservedName {$r = CANNOT_EVAL}	                    # FullQualifiedName
	| expression = oclExp argExp {$r = CANNOT_EVAL}					                    # CallExpression
	| expression = oclExp '.' attname = unrestrictedName argExp {$r = CANNOT_EVAL}		# MethodCall
	| expression = oclExp '.' attname = unrestrictedName {$r = CANNOT_EVAL}			    # AttributeNavigation
	| expression = oclExp '->' attname = unrestrictedName argExp {$r = CANNOT_EVAL}	    # CollectionCall
	| operator = '-' expression = oclExp {$r = f(($expression.r,), ((int, float),), lambda n: -n)}                      # UnaryOperation
	| operator = 'not' expression = oclExp {$r = f(($expression.r,), (bool,), lambda n: not n)}					        # UnaryOperation
	| left = oclExp operator = '*' right = oclExp {$r = f(($left.r, $right.r), (int, int), lambda l, r: l * r)}		    # ArithmeticBinaryOperation
	| left = oclExp operator = '/' right = oclExp {$r = f(($left.r, $right.r), (int, int), lambda l, r: l / r)}			# ArithmeticBinaryOperation
	| left = oclExp operator = '+' right = oclExp {$r = f(($left.r, $right.r), (int, int), lambda l, r: l + r)}         # ArithmeticBinaryOperation
	| left = oclExp operator = '-' right = oclExp {$r = f(($left.r, $right.r), (int, int), lambda l, r: l - r)}	        # ArithmeticBinaryOperation
	| left = oclExp operator = '<' right = oclExp {$r = f(($left.r, $right.r), (OBJ, OBJ), lambda l, r: l < r)} 		# ComparisonBinaryOperation
	| left = oclExp operator = '>' right = oclExp {$r = f(($left.r, $right.r), (OBJ, OBJ), lambda l, r: l > r)} 		# ComparisonBinaryOperation
	| left = oclExp operator = '<=' right = oclExp {$r = f(($left.r, $right.r), (OBJ, OBJ), lambda l, r: l <= r)} 		# ComparisonBinaryOperation
	| left = oclExp operator = '>=' right = oclExp {$r = f(($left.r, $right.r), (OBJ, OBJ), lambda l, r: l >= r)} 		# ComparisonBinaryOperation
	| left = oclExp operator = '=' right = oclExp {$r = f(($left.r, $right.r), (OBJ, OBJ), lambda l, r: l == r)} 		# ComparisonBinaryOperation
	| left = oclExp operator = '<>' right = oclExp {$r = f(($left.r, $right.r), (OBJ, OBJ), lambda l, r: l != r)} 		# ComparisonBinaryOperation
	| left = oclExp operator = 'and' right = oclExp {$r = f(($left.r, $right.r), (bool, bool), lambda l, r: l and r)}   # BooleanBinaryOperation
	| left = oclExp operator = 'or' right = oclExp {$r = f(($left.r, $right.r), (bool, bool), lambda l, r: l or r)}	    # BooleanBinaryOperation
	| left = oclExp operator = 'xor' right = oclExp																	    # BooleanBinaryOperation
	| left = oclExp operator = 'implies' right = oclExp																	# BooleanBinaryOperation;

argExp:
	'(' (body += oclExp (',' body += oclExp)*)? ')' # ArgumentsExp
	| '(' varnames += unreservedName (
		',' varnames += unreservedName
	)* (':' typeExpCS)? (
		';' iterator = unreservedName (':' typeExpCS)? '=' initializer = oclExp
	)? '|' body = oclExp ')' # LambdaExp;

primaryExp
	returns[r]:
	selfExp
	| n_ = nestedExp {$r = $n_.r}
	| n = primitiveLiteralExp {$r = $n.r}
	| tupleLiteralExp
	| collectionLiteralExp
	| typeLiteralExp
	| letExp
	| ifExp;

selfExp: 'self';

nestedExp returns [r]: '(' nested = oclExp ')' {$r = $nested.r};

primitiveLiteralExp
	returns[r]:
	n = numberLiteralExpCS {$r = $n.r}					# NumberLiteral
	| n = booleanLiteralExpCS {$r = $n.text == 'true'}	# BooleanLiteral
	| n = stringLiteralExpCS {$r = $n.text}				# StringLiteral
	| unlimitedNaturalLiteralCS {$r = CANNOT_EVALUTATE}	# UnlimitedNaturalLiteral
	| invalidLiteralExpCS {$r=None}						# InvalidLiteral
	| nullLiteralExpCS {$r=None}						# NullLiteral;

tupleLiteralExp:
	'Tuple' '{' tupleLiteralPartCS (',' tupleLiteralPartCS)* '}';

tupleLiteralPartCS:
	unrestrictedName (':' typeExpCS)? '=' primaryExp;

collectionLiteralExp:
	collectionTypeCS '{' (
		expressions += collectionLiteralPartCS (
			',' expressions += collectionLiteralPartCS
		)*
	)? '}';

collectionTypeCS:
	collectionTypeIdentifier (
		'(' typeExpCS ')'
		| '<' typeExpCS '>'
	)?;

primitiveTypeCS:
	'String'				# StringType
	| 'Integer'				# IntegerType
	| 'UnlimitedNatural'	# UnlimitedNaturalType
	| 'Boolean'				# BooleanType
	| 'Real'				# RealType
	| 'OclAny'				# OCLAnyType
	| 'OclInvalid'			# OCLInvalidType
	| 'OclMessage'			# OCLMessage
	| 'OclSelf'				# OCLSelf
	| 'OclVoid'				# OCLVoid;

collectionTypeIdentifier:
	'Collection'	# CollectionType
	| 'Bag'			# BagType
	| 'OrderedSet'	# OrderedSetType
	| 'Sequence'	# SequenceType
	| 'Set'			# SetType;

collectionLiteralPartCS:
	oclExp
	| inf = oclExp isInterval = '..' sup = oclExp;

typeLiteralExp: typeLiteralCS;

letExp:
	'let' variables += letVariableCS (
		',' variables += letVariableCS
	)* 'in' oclExp;

letVariableCS: unrestrictedName (':' typeExpCS)? '=' oclExp;

typeExpCS: typeLiteralCS | typeNameExpCS;

typeNameExpCS:
	unrestrictedName
	| typeNameExpCS ('::' unreservedName)+;

typeLiteralCS: collectionTypeCS | primitiveTypeCS | tupleTypeCS;

tupleTypeCS:
	'Tuple' (
		'(' tuplePartCS (',' tuplePartCS)* ')'
		| '<' tuplePartCS (',' tuplePartCS)* '>'
	)?;

tuplePartCS: unrestrictedName ':' typeExpCS;

ifExp returns [r]:
	'if' condition = oclExp 'then' body = oclExp 'else' else_ = oclExp 'endif';

numberLiteralExpCS
	returns[r]:
	INT {$r=int($INT.text)}
	| FLOAT {$r=float($FLOAT.text)};

stringLiteralExpCS: STRING;

booleanLiteralExpCS: 'true' | 'false';

unlimitedNaturalLiteralCS: '*';

invalidLiteralExpCS: 'invalid';

nullLiteralExpCS: 'null';

unrestrictedName:
	~(
		'('
		| ')'
		| 'true'
		| 'false'
		| 'and'
		| 'else'
		| 'endif'
		| 'false'
		| 'if'
		| 'implies'
		| 'in'
		| 'invalid'
		| 'let'
		| 'not'
		| 'null'
		| 'or'
		| 'self'
		| 'then'
		| 'true'
		| 'xor'
		| 'Bag'
		| 'Boolean'
		| 'Collection'
		| 'Integer'
		| 'Lambda'
		| 'OclAny'
		| 'OclInvalid'
		| 'OclMessage'
		| 'OclSelf'
		| 'OclVoid'
		| 'OrderedSet'
		| 'Real'
		| 'Sequence'
		| 'Set'
		| 'String'
		| 'Tuple'
		| 'UnlimitedNatural'
	);
unreservedName:
	~(
		'('
		| ')'
		| 'and'
		| 'else'
		| 'endif'
		| 'false'
		| 'if'
		| 'implies'
		| 'in'
		| 'invalid'
		| 'let'
		| 'not'
		| 'null'
		| 'or'
		| 'self'
		| 'then'
		| 'true'
		| 'xor'
	);

STRING: '\'' ~[']* '\'';
SPECIAL_VARNAME: '_' STRING;
VARNAME: [a-zA-Z_][a-zA-Z_0-9]*;
INT: [0-9]+;
FLOAT: INT ('.' INT)? (('e' | 'E') ('+' | '-')? INT)?;

// COMMENT:LINE_COMMENT|BLOCK_COMMENT|DOCU_COMMENT; LINE_COMMENT:'--' .*? '\n'; BLOCK_COMMENT: '/*'
// .*? '*/'; DOCU_COMMENT: '/**' .*? '*/';
WS: [ \n\t\r]+ -> skip;