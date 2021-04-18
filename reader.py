from pyecoreocl.compiler import dummy_compiler

expression = "let x = Set{0, 1..15} in x->select(e | e > 0)->collect(e | e + 4)"
print(dummy_compiler(expression))

expression = "Sequence{0, 1..15}->select(e | e > 0)->collect(e | e + 4)"
print(dummy_compiler(expression))

expression = "Set{}->isEmpty(4)"
print(dummy_compiler(expression))

expression = "len(x, (y+4) * 3)"
print(dummy_compiler(expression))

expression = "a.b.c.d(45)"
print(dummy_compiler(expression))

expression = "let x = Tuple{foo='abc'} in x.foo"
print(dummy_compiler(expression))

expression = "ParameterDirectionKind::inout"
print(dummy_compiler(expression))

expression = """(if nestingClass > null then null
else
let b:BehavioredClassifier = self.behavioredClassifier(self.owner) in
    if b.oclIsKindOf(Behavior) and b.oclAsType(Behavior).context > null then
            b.oclAsType(Behavior).context
                else b endif endif)"""
print(dummy_compiler(expression))
