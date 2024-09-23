generate-grammar: pyecoreocl/parser/OclExpressionParser.py

pyecoreocl/parser/OclExpressionParser.py: OclExpression.g4
	antlr4 -visitor -listener -Dlanguage=Python3 OclExpression.g4 -o pyecoreocl/parser


clean:
	rm -f pyecoreocl/parser/OclExpression*

test:
	python -m pytest -s

cache_clean_test:
	rm -rf tests/__pycache__ && python -m pytest -s