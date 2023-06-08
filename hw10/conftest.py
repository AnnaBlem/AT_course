import pytest
import datetime


@pytest.fixture()
def start_end():
    """
    печать времени начала выполнения класса с тестами и окончания
    """
    dt_start = datetime.datetime.now()
    dt__start_formatted = dt_start.strftime('%d.%m %H:%M:%S')
    print(f'время начала выполнения класса {dt__start_formatted}')

    yield

    dt_end = datetime.datetime.now()
    dt__end_formatted = dt_end.strftime('%d.%m %H:%M:%S')
    print(f'время окончания выполнения класса {dt__end_formatted}')


@pytest.fixture()
def execution_time():
    """
    время выполнения теста
    """
    dt_start = datetime.datetime.now()
    yield
    dt_end = datetime.datetime.now()
    diff = dt_end - dt_start
    print(f'время выполнения теста {diff}')


