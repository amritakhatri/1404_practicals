"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in.
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_sentence(phrase):
    """
    Format a phrase as a sentence.
    >>> format_sentence('hello')
    'Hello.'
    >>> format_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_sentence('this is a test')
    'This is a test.'
    """
    return phrase.capitalize().rstrip('.') + '.'


def run_tests():
    """Run the tests on the functions."""
    # Test repeat_string function
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    # Test Car class functionality
    car_default = Car()
    assert car_default.fuel == 0, "Car does not default fuel to 0"

    car_custom = Car(fuel=10)
    assert car_custom.fuel == 10, "Car does not set custom fuel correctly"


run_tests()

# Run doctests
doctest.testmod()
