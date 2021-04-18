# PyEcoreOCL: OCL to Python compiler

This project aims to provide an Object Constraint Language (OCL) to Python compiler.
The project is takes inspiration on the work of [Anthony Beuchey](https://github.com/Beuchey) that wrote a [textX](https://github.com/textX/textX) grammar for OCL and a set of wrappers that enables OCL api on Python objects, as well as on the work of [CrossEcore](https://github.com/crossecore) about the grammar for [OCLInEcore](https://github.com/crossecore/oclinecore).

This parser will be used to parse OCL expressions in `.ecore` documentation and automatically fill python implementation when possible (I see you UML2 ecore files :smile:).



## Usage

Currently in dev., only a dumb transpiler is doing the work, no semantic analysis, no constant propagation, nothing.
It just transpile your OCL expression without doing optimization or anything and translates toward only one expression, no multi-statements.
Consequently, `let ... in ...` expressions are translated in `lambda`.

```python
expression = "let x = Set{0, 1..15} in x->select(e | e > 0)->collect(e | e + 4)"
print(dummy_compiler(expression))
# result
(lambda x: [e + 4 for e in [e for e in x if e > 0]])({0, *range(1, 15), }, )

expression = "Sequence{0, 1..15}->select(e | e > 0)->collect(e | e + 4)"
print(dummy_compiler(expression))
# result
[e + 4 for e in [e for e in [0, *range(1, 15), ] if e > 0]]

expression = "Set{}->isEmpty(4)"
print(dummy_compiler(expression))
# result
len(set()) == 0

expression = "len(x, (y+4) * 3)"
print(dummy_compiler(expression))
# result
len(x, (y + 4) * 3)

expression = "a.b.c.d(45)"
print(dummy_compiler(expression))
# result
a.b.c.d(45)

expression = "let x = Tuple{foo='abc'} in x.foo"
print(dummy_compiler(expression))
# result
(lambda x: x.foo)(OCLTuple(foo='abc'))

expression = "ParameterDirectionKind::inout"
print(dummy_compiler(expression))
# result
ParameterDirectionKind.inout

expression = """(if nestingClass > null then null
else
let b:BehavioredClassifier = self.behavioredClassifier(self.owner) in
    if b.oclIsKindOf(Behavior) and b.oclAsType(Behavior).context > null then
            b.oclAsType(Behavior).context
                else b endif endif)"""
print(dummy_compiler(expression))
# result
(None if nestingClass > None else (lambda b: b.context if isinstance(b, Behavior) and b.context > None else b)(self.behavioredClassifier(self.owner)))


expression = """Extension.allInstances()->select(ext |  let endTypes = ext.memberEnd->collect(e | type.oclAsType(Classifier)) in
        endTypes->includes(self) or endTypes.allParents()->includes(self))"""
print(dummy_compiler(expression))
# result
[ext for ext in Extension.allInstances() if (lambda endTypes: self in endTypes or self in endTypes.allParents())([type for e in ext.memberEnd])]
```

## Dependencies

* antlr4
