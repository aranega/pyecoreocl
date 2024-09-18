# coding: magic_ocl.strict
"""
This test module goal is to test all functions over collections
"""

from dataclasses import dataclass
from gc import collect
import itertools
from operator import indexOf
from typing import Sequence


def test__basic_collections():
    assert !Sequence{3}! == [3]
    assert !Bag{3}! == [3]
    assert !Set{3}! == {3}

    assert !Sequence{}! == []
    assert !Bag{}! == []
    assert !Set{}! == set()

    assert !Sequence(int){3}! == [3]
    assert !Bag(int){3}! == [3]
    assert !Set(int){3}! == {3}

    assert !Sequence<int>{3}! == [3]
    assert !Bag<int>{3}! == [3]
    assert !Set<int>{3}! == {3}


def test__as_sequence():
    assert !Sequence{3}->asSequence()! == [3]
    assert !Bag{4}->asSequence()! == [4]
    assert !Set{5}->asSequence()! == [5]
    assert !OrderedSet{6}->asSequence()! == [6]


def test__as_bag():
    assert !Sequence{3}->asBag()! == [3]
    assert !Bag{4}->asBag()! == [4]
    assert !Set{5}->asBag()! == [5]
    assert !OrderedSet{6}->asBag()! == [6]


def test__as_bag():
    assert !Sequence{3}->asSet()! == {3}
    assert !Bag{4}->asSet()! == {4}
    assert !Set{5}->asSet()! == {5}
    assert !OrderedSet{6}->asSet()! == {6}


def test__collect():
    l = [3, 4, 5]
    assert !l->collect(e: int | e + 1)->asSequence()! == [4, 5, 6]

    l = !Sequence{Tuple{value=3}, Tuple{value=4}, Tuple{value='stuff'}}!
    assert !l->collect(e | e.value)->asSequence()! == [3, 4, "stuff"]

    l = [3, 4, 5]
    assert !l->collect(e: int | Sequence{e})->asSequence()! == [3, 4, 5]


def test__collect_nested():
    l = [3, 4, 5]
    assert !l->collectNested(e: int | e + 1)->asSequence()! == [4, 5, 6]

    l = !Sequence{Tuple{value=3}, Tuple{value=4}, Tuple{value='stuff'}}!
    assert !l->collectNested(e | e.value)->asSequence()! == [3, 4, "stuff"]

    l = [3, 4, 5]
    assert !l->collectNested(e: int | Sequence{e})->asSequence()! == [[3], [4], [5]]

    l = [3, 4, 5]
    assert !l->collectNested(e: int | Sequence{Sequence{e}})->asSequence()! == [[[3]], [[4]], [[5]]]


def test__any():
    l = [3, 4, 5]
    assert !l->any()! == 3

    assert !Bag{3, 4, 5}->collect(e | e + 1)->any()! == 4


def test__exists():
    l = [3, 4, 5]
    assert !l->exists(e | e = 3)! is True

    assert !Bag{3, 4, 5}->collect(e | e + 1)->exists(e | e = 3)! is False


def test__one():
    l = [3, 4, 5]
    assert !l->one(e | e = 3)! is True

    assert !Bag{3, 4, 5}->collect(e | e + 1)->one(e | e = 3)! is False


def test__sorted_by():
    l = [3, 4, 5]
    assert !l->sortedBy(e | -e)! == [5, 4, 3]


def test__including():
    assert !Set{1, 2}->including(1)->asSet()! == {1, 2}
    assert !Set{1, 2}->including(3)->asSet()! == {1, 2, 3}

    assert !Set{1, 2}->including(1)->asSequence()! == [1, 2, 1]
    assert !Set{1, 2}->including(3)->asSequence()! == [1, 2, 3]


def test__excluding():
    assert !Set{1, 2}->excluding(1)->asSet()! == {2}
    assert !Set{1, 2}->excluding(3)->asSet()! == {1, 2}

    assert !Set{1, 2}->excluding(2)->asSequence()! == [1]
    assert !Set{1, 2}->excluding(3)->asSequence()! == [1, 2]


def test__iterate():
    assert !Sequence{1, 2, 3}->iterate(e, acc = Sequence{} | acc->including(e + 1))->asSequence()! == [2, 3, 4]


def test__select_by_kind():
    assert !Sequence{'c', 1, 3, 'd'}->selectByKind(str)->asSequence()! == ['c', 'd']

    @dataclass
    class X:
        ...

    @dataclass
    class A(X):
        ...

    @dataclass
    class B(X):
        ...

    l = [A(), A(), B(), B()]
    assert !l->selectByKind(A)->asSequence()! == l[:2]
    assert !l->selectByKind(B)->asSequence()! == l[2:]
    assert !l->selectByKind(X)->asSequence()! == l


def test__select_by_type():
    assert !Sequence{'c', 1, 3, 'd'}->selectByType(str)->asSequence()! == ['c', 'd']

    @dataclass
    class X:
        ...

    @dataclass
    class A(X):
        ...

    @dataclass
    class B(X):
        ...

    l = [A(), A(), B(), B()]
    assert !l->selectByType(A)->asSequence()! == l[:2]
    assert !l->selectByType(B)->asSequence()! == l[2:]
    assert !l->selectByType(X)->asSequence()! == []


def test__append():
    assert !Set{1, 2}->append(1)->asSet()! == {1, 2}
    assert !Set{1, 2}->append(3)->asSet()! == {1, 2, 3}

    assert !Set{1, 2}->append(1)->asSequence()! == [1, 2, 1]
    assert !Set{1, 2}->append(3)->asSequence()! == [1, 2, 3]


def test__prepend():
    assert !Set{1, 2}->prepend(1)->asSet()! == {1, 2}
    assert !Set{1, 2}->prepend(3)->asSet()! == {1, 2, 3}

    assert !Set{1, 2}->prepend(1)->asSequence()! == [1, 1, 2]
    assert !Set{1, 2}->prepend(3)->asSequence()! == [3, 1, 2]


def test__first():
    assert !Sequence{1, 2}->first()! == 1
    assert !Sequence{1, 2}->collect(e | e + 1)->first()! == 2


def test__last():
    assert !Sequence{1, 2}->last()! == 2
    assert !Sequence{1, 2}->collect(e | e + 1)->last()! == 3


def test__index_of():
    assert !Sequence{1, 2}->indexOf(2)! == 1
    assert !Sequence{1, 2}->collect(e | e + 1)->indexOf(2)! == 0
