# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3

import pytest


@pytest.mark.id_check(1, 2, 3)
def test():
    id_check_args = next(m.args for m in test.pytestmark if m.name == 'id_check')
    print(*id_check_args, sep=', ')
