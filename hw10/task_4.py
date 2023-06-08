# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.usefixtures('start_end')
class Tests:

    @pytest.mark.usefixtures('execution_time')
    def test_all_positive(self):
        assert all_division(4, 2) == 2

    def test_zero_1st(self):
        assert all_division(0, 2) == 0

    def test_negative(self):
        assert all_division(-2, 2) == -1

    def test_3_elements(self):
        assert all_division(2, 4, 1) == 0.5

    def test_zero_2nd(self):
        with pytest.raises(ZeroDivisionError):
            all_division(2, 0)

