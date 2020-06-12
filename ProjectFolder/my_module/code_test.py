import pytest

from mergesort_functions import check_input
from mergesort_functions import change_to_int

def test_check_input_with_numbers():
    assert check_input(['1', '3', '2', '4']) == False

def test_check_input_with_numbers_and_letters():
    assert check_input(['1', '3', '2', 'fdsafsd']) == True

def test_check_input_with_letters():
    assert check_input(['fdsa', 'dfa', 'fdsafsd']) == True

def test_check_input_with_only_one_element():
    assert check_input(['1']) == True

def test_check_input_with_zero_elements():
    assert check_input([]) == True


def test_change_to_int():
    assert change_to_int(['1', '3', '2', '4']) == [1, 3, 2, 4]
