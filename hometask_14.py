import doctest
import unittest

import pytest


# Напишите код, который запрашивает число и сообщает являться ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на
# единицу и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
def is_simple(num: int or float) -> bool or str:
    """The additional intel for testing this func
    >>> is_simple(3)
    True
    >>> is_simple(666)
    False
    >>> is_simple(-5)
    'Sorry, dude, your number is invalid'
    """
    if num < 0 or num > 100000:
        return 'Sorry, dude, your number is invalid'
    else:
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        return count <= 2


class TestFirstTask(unittest.TestCase):

    def test_case(self):
        self.assertTrue(is_simple(17), msg=True)


@pytest.mark.parametrize('number, result', [(666, True),
                                            (1488, True),
                                            (27, False)])
def test_first_task(number, result):
    assert is_simple(number) == result, 'Something went wrong'


# Функция получает целое число, систему исчисления и возвращает его строковое представление.
def get_number(number: int, mod: int = 10) -> str:
    """
    >>> get_number(123, 2)
    '1111011'
    >>> get_number(123, 3)
    '11120'
    >>> get_number(123, 4)
    '1323'
    >>> get_number(123, 5)
    '443'
    >>> get_number(123, 6)
    '323'
    >>> get_number(123, 7)
    '234'
    >>> get_number(123, 8)
    '173'
    >>> get_number(123, 9)
    '146'
    """
    result = ''
    while number != 0:
        result = str(number % mod) + result
        number //= mod
    return result


class TestSecondTask(unittest.TestCase):

    def test_case(self):
        self.assertTrue(get_number(17), msg='17')


@pytest.mark.parametrize('numb, val', [(666, '666'),
                                       (1488, '1488'),
                                       (27, '27')])
def test_second_task(numb, val):
    assert is_simple(numb) == val, 'Something went wrong'


if __name__ in '__main__':
    doctest.testmod(verbose=True)
    unittest.main(verbosity=True)
    pytest.main()
