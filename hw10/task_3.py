# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('a, b, result', [
    pytest.param(4, 2, 2, marks=pytest.mark.smoke),
    pytest.param(0, 2, 0, marks=pytest.mark.skip('skipped')),
    (-2, 2, -1)])
def test_3(a, b, result):
   assert all_division(a, b) == result






