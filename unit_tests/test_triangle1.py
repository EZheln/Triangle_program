import unittest

from main import triangle1

def test_def_small_test_1():
    one_value = triangle1.def_small_test(0,0,0)
    assert one_value == 4

def test_def_small_test_2():
    second_value = triangle1.def_small_test(12,12,5)
    assert second_value == 2

def test_def_small_test_3():
    third_value = triangle1.def_small_test(8,25,18)
    assert third_value == 1

def test_def_small_test_4():
    fourth_value = triangle1.def_small_test(25,25,25)
    assert fourth_value == 3


