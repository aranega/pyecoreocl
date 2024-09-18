# coding: magic_ocl.strict
"""
This test module goal is to test all functions over collections
"""

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
