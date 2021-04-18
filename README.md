# PyEcoreOCL: OCL to Python compiler

This project aims to provide an Object Constraint Language (OCL) to Python compiler.
The project is takes inspiration on the work of [Anthony Beuchey](https://github.com/Beuchey) that wrote a [textX](https://github.com/textX/textX) grammar for OCL and a set of wrappers that enables OCL api on Python objects, as well as on the work of [CrossEcore](https://github.com/crossecore) about the grammar for [OCLInEcore](https://github.com/crossecore/oclinecore).


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
```

## Dependencies

* antlr4
