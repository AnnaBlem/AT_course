# Напишите декоратор func_log, который может принимать аргумент file_log (Путь до файла), по умолчнию равен 'log.txt'
# Декоратор должен дозаписывать в файл имя вызываемой функции (можно получить по атрибуту __name__), дату и время вызова
# по формату:
# имя_функции вызвана %d.%m %H:%M:%S
# Для вывода времени нужно использовать модуль datetime и метод .strftime()
# https://pythonworld.ru/moduli/modul-datetime.html
# https://docs.python.org/3/library/datetime.html
#
# Например
# @func_log()
# def func1():
#     time.sleep(3)
#
# @func_log(file_log='func2.txt')
# def func2():
#     time.sleep(5)
#
# func1()
# func2()
# func1()
#
# Получим:
# в log.txt текст:
# func1 вызвана 30.05 14:12:42
# func1 вызвана 30.05 14:12:50
# в func2.txt текст:
# func2 вызвана 30.05 14:12:47

# Со звёздочкой. ДЕЛАТЬ НЕ ОБЯЗАТЕЛЬНО.
# help(func1) должен выводит одинаковый текст, когда есть декоратор на функции func1 и когда его нет
# Реализовать без подключения новых модулей и сторонних библиотек.


import datetime
# Здесь пишем код


def write_log(file_log, func_name):
    dt = datetime.datetime.now()
    dt_formatted = dt.strftime('%d.%m %H:%M:%S')
    with open(file_log, mode='a', encoding='utf-8') as file:
        file.write(f'{func_name} вызвана {dt_formatted}\n')


def func_log(file_log='log.txt'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            write_log(file_log, func.__name__)
            return func(*args, **kwargs)
        attrs = ['__name__', '__doc__', '__qualname__', '__defaults__', '__kwdefaults__', '__annotations__',
                 '__module__']
        for attr in attrs:
            if hasattr(func, attr):
                setattr(wrapper, attr, getattr(func, attr))
        wrapper.__dict__.update(func.__dict__)
        return wrapper
    return decorator





import time
# @func_log()
# def func1():
#     time.sleep(1)
#
# @func_log(file_log='func2.txt')
# def func2():
#     time.sleep(2)
#
# func1()
# func2()
# func1()




