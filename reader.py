from pyecoreocl.compiler import dummy_compiler

expression = "let x = Set{0, 1..15} in x->select(e | e > 0)->collect(e | e + 4)"
print(dummy_compiler(expression))

expression = "Sequence{0, 1..15}->select(e | e > 0)->collect(e | e + 4)"
print(dummy_compiler(expression))
