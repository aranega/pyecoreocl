# PyEcoreOCL: OCL to Python compiler

This project aims to provide an Object Constraint Language (OCL) to Python compiler.
This parser will be used to parse OCL expressions in `.ecore` documentation and automatically fill python implementation when possible.
The project also includes a way to directly inline OCL code in Python code: the OCL code is compiled in Python code and directly embedded in the Python code line.
The inline OCL code can reference Python objects (Python variables and functions in your code) and the execution returns Python object that can be directly manipulated by Python.
PyEcoreOCL is compatible with PyEcore, but PyEcore is a dependency or a requirement.
PyEcoreOCL can take full Python objects and do not relies on PyEcore objects, unless some specific operations implying EMF related operations are used.

The project is takes inspiration on the work of [Anthony Beuchey](https://github.com/Beuchey) that wrote a [textX](https://github.com/textX/textX) grammar for OCL and a set of wrappers that enables OCL api on Python objects, as well as on the work of [CrossEcore](https://github.com/crossecore) about the grammar for [OCLInEcore](https://github.com/crossecore/oclinecore).

## Installation

Currently, there is no dedicated distribution on pypi, so the way to install is to perform the classical pip install command from the repository directory.

```bash
pip install .
```

or, if you want it in "edit" mode:

```bash
pip install -e .
```

## Dependencies

* `antlr4-python3-runtime`
* `magic_codec` (for embedded OCL)
* for the repl: `pyecore`

## Usage

There is two main usage for the compiler:

* as string to string, taking OCL code and returning the equivalent compiled Python expression,
* directly inlining OCL expressions in Python code.

Currently, only a dumb transpiler is doing the work, no semantic analysis, no constant propagation, just a pure translation of what you wrote in your OCL expression.
It just transpile your OCL expression in only one Python expression, trying to match as much as possible the OCL semantic (e.g: `let ... in ...` expressions are translated in `lambda`).

### String to String

Here is a simple usage example:

```python
from pyecoreocl import dummy_compiler

python_code = dummy_compiler("let x = Tuple{foo='abc'} in x.foo")
print(python_code)
```

The compiler as two modes `normal` and `strict`.
In `strict` mode, implicit collect over collections is not enabled, consequently, a line like this one:

```
Persons.allInstances().name
```

will be translated in this, depending on the compiler mode:

```python
# Caution: "allInstances()" is only available on PyEcore metaclasses
# in normal mode
ocl.geta(Persons.allInstances(), "name")

# Caution: "allInstances()" is only available on PyEcore metaclasses
# in strict mode
Persons.allInstances().name
```

### Inlined OCL in Python code

To inline some OCL in Python code, you need to define first `# coding: magic_ocl` as encoding as first line of your Python file.
This will enable the special codec that is responsible for extracting the OCL expressions, to compile them, and inline them in the Python code.

Here is a simple example using a Python dataclass, defining some operations on the dataclass:

```python
# coding: magic_ocl
from dataclasses import dataclass

@dataclass
class Student:
    notes: list[float]
    name: str

    @property
    def notes_valid(self):
        return !self.notes->forAll(e | e > 0)!

    @property
    def is_semester_validated(self):
        return !self.notes_valid and (self.notes->sum() / self.notes->size()) > 10!


s1 = Student(name="S1", notes=[10.0, 9.0, 18.5, 20.0])
print("Student validated semester?", s1.is_semester_validated)
```

Here is a slightly mode complex example using a PyEcore class:

```python
# coding: magic_ocl
from pyecore.ecore import *

@EMetaclass
class Student(object):
    notes = EAttribute(eType=EFloat, upper=-1)
    name = EAttribute(eType=EString)

    def __init__(self, name=None, notes=None):
        if notes:
            self.notes.extend(notes)
        self.name = name

    @property
    def notes_valid(self):
        return !self.notes->forAll(e | e > 0)!

    @property
    def is_semester_validated(self):
        return !self.notes_valid and (self.notes->sum() / self.notes->size()) > 10!


s1 = Student(name="s1", notes=[10.5, 1.4, 4.5])
s2 = Student(name="s1", notes=[10.5, 1.4, 4.5])

print("All names different?", !Student.allInstances()->forAll( e1, e2 : Student | e1 <> e2 implies e1.name <> e2.name)!)
```

As the OCL code is directly inlined in the Python code once compiled, you can reference Python variables and functions in your OCL code, and you can manipulate the result of the OCL expression diretly in Python:

```python
# coding: magic_ocl

from random import randint
from itertools import islice

# We reference upper_value and use randint from Python in our OCL expression
upper_value = 50
lst = list(!let x = Set{2..upper_value} in x->select(e | e > randint(2, upper_value))!)
print(lst)
print(lst[::2])

# We maniulate directly the result of the OCL expression with islice
result = !Set{2..upper_value}->select(e | e > randint(2, upper_value))!
print(list(islice(result, None, None, 2)))

# We directly get some items from the OCL expression result (the OCL expression uses "list" from Python)
print(!list(Set{2..upper_value}->select(e | e > randint(2, upper_value)))![::2])
```

NOTE: Please note that currently, only OCL expressions that fits on 1 line are supported.
Multiline OCL expressions are not yet supported in inlined OCL.

## Translation Examples (strict mode)

```
OCL:    let x = Set{0, 1..15} in x->select(e | e > 0)->collect(e | e + 4)
Python: (lambda x: [e + 4 for e in [e for e in x if e > 0]])({0, *range(1, 15), }, )

OCL:    Sequence{0, 1..15}->select(e | e > 0)->collect(e | e + 4)
Python: [e + 4 for e in [e for e in [0, *range(1, 15), ] if e > 0]]

OCL:    Set{}->isEmpty(4)
Python: len(set()) == 0

OCL:    len(x, (y+4) * 3)
Python: len(x, (y + 4) * 3)

OCL:    a.b.c.d(45)
Python: a.b.c.d(45)

OCL:    let x = Tuple{foo='abc'} in x.foo
Python: (lambda x: x.foo)(OCLTuple(foo='abc'))

OCL:    ParameterDirectionKind::inout
Python: ParameterDirectionKind.inout

OCL:    (if nestingClass > null then null
        else
        let b:BehavioredClassifier = self.behavioredClassifier(self.owner) in
                if b.oclIsKindOf(Behavior) and b.oclAsType(Behavior).context > null then
                        b.oclAsType(Behavior).context
                                else b endif endif)
Python: (None if nestingClass > None else (lambda b: b.context if isinstance(b, Behavior) and b.context > None else b)(self.behavioredClassifier(self.owner)))


OCL:    Extension.allInstances()->select(ext |  let endTypes = ext.memberEnd->collect(e | type.oclAsType(Classifier)) in
                endTypes->includes(self) or endTypes.allParents()->includes(self))
Python: [ext for ext in Extension.allInstances() if (lambda endTypes: self in endTypes or self in endTypes.allParents())([type for e in ext.memberEnd])]
```


## Toy Example

This repository proposes a very simple repl for OCL expressions.
Launch it using `python oclrepl.py`.
You'll get a repl interface running.
You can either type an ocl expression directly, or load a metamodel/model and register metamodels (requires `pyecore`).

Syntax to load a model/metamodel is: `load <model_metamodel_path.ecore>`.
Syntax to register a metamodel is: `register <model_metamodel_path.ecore>`.

Here is a demo on how to use it.

![](repl_demo.svg)


## Limitations

Currently, some expressions are not well recognized, or not properly compiled:

* `obj->operation()`: in the specification, `->` acts as an automatic wrapper to a `Sequence` if `obj` is not a collection. Currently, PyEcoreOCL doesn't consider this automatic wrapping.
* `collection->collect(attr)`: when there is no variable that is considered by the lambda inside collection operations, by default `attr` should be considered as attribute of an implicit `self` variable representing at each iteration one of the elements of `collection`. Currently, this is not supported, and it's not sure it will be for inline OCL. To overcome this, it's currently necessary to explicitally name the variable inside the lambda `collection->collect(e | e.attr)`.