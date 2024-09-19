# coding: magic_ocl.strict
"""
This test module goal is to test all functions over primitive types
"""

from dataclasses import dataclass
from operator import indexOf


def test__string_size():
    assert !'abc'.size()! == 3


def test__is_kind_ok():
    assert !'abc'.oclIsKindOf(str)! is True


def test__is_type_of():
    assert !'abc'.oclIsTypeOf(str)! is True


def test___as_type():
    assert !'abc'.oclAsType(str)! == 'abc'


def test__concat():
    assert !'abc'.concat('def')! == "abcdef"


def test__substring():
    assert !'abcd'.substring(1, 2)! == "bc"


def test__to_integer():
    assert !'12'.toInteger()! == 12


def test__to_real():
    assert !'12'.toReal()! == 12.0


def test__string_upper_case():
    assert !'abc'.toUpperCase()! == 'ABC'


def test__string_lower_case():
    assert !'ABC'.toLowerCase()! == 'abc'


def test__string_index_of():
    assert !'abc'.indexOf('b')! == 1


def test__string_equals_ignore_case():
    assert !'abc'.equalsIgnoreCase('AbC')! is True


def test__string_at():
    assert !'abc'.at(1)! == "b"


def test__string_characters():
    assert !'abc'.characters()! == ['a', 'b', 'c']


def test__to_boolean():
    assert !'True'.toBoolean()! is True
    assert !'False'.toBoolean()! is False