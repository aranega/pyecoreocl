# coding: magic_ocl.strict
"""
This test module goal is to test all basic constructions of the language.
"""
import builtins
import pytest


def test__let_with_numbers():
    assert !let x = 4 in x! == 4
    assert !let x = 4 in x + 1! == 5
    assert !let x = 4 in let y = 2 in x + y! == 6
    assert !let x = 4 in let y = x - 1 in x + y! == 7

    x = !8!
    assert !let x = x in x! == 8

    x = !9!
    assert !let y = x in x! == 9


def test__let_with_objects():
    assert !let x = print in x! == print
    assert !let x = builtins.getattr in x! == builtins.getattr
    assert !let x = 'C' in isinstance(x, str)! is True


def test__implicit_collect():
    l = !Sequence{Tuple{value=3}, Tuple{value=4}, Tuple{value='stuff'}}!
    assert !l->at(0).value! == 3
    assert !l->at(1).value! == 4
    assert !l->at(2).value! == "stuff"

    with pytest.raises(AttributeError):
        assert !l.value->asSequence()! == [3, 4, "stuff"]


def test__if_then_else():
    assert (!if true then false else true endif!) is False
    assert (!if true or false then 3 else 4 endif!) == 3
    assert (!if 3 <> 3 then 3 else 4 endif!) == 4


def test__booleans():
    assert !true! is True
    assert !false! is False

    assert (!not true!) is False
    assert (!not false!) is True

    assert !(true or true)! is True
    assert !(true or false)! is True
    assert !(false or true)! is True
    assert !(false or false)! is False

    assert (!true and true!) is True
    assert (!true and false!) is False
    assert (!false and true!) is False
    assert (!false and false!) is False

    assert (!true implies false!) is False
    assert (!false implies true!) is True
