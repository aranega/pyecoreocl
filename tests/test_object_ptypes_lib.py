# coding: magic_ocl.strict
"""
This test module goal is to test all functions over primitive types
"""

from dataclasses import dataclass


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