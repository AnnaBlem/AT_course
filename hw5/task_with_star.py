# Напишите функцию to_roman, которая преобразуют арабское число (val) в римское (roman_str).
#
# Современные римские цифры записываются, выражая каждую цифру отдельно,
# начиная с самой левой цифры и пропуская цифру со значением нуля.
# Римскими цифрами 1990 отображается: 1000=М, 900=СМ, 90=ХС; в результате MCMXC.
# 2023 записывается как 2000=MM, 20=XX, 3=III; или MMXXIII.
# В 1666 используется каждый римский символ в порядке убывания: MDCLXVI.
#
# Например (Ввод --> Вывод) :
# 2008 --> MMVIII


arab_rome = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
             10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
             100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
             1000: 'M'
             }


def to_roman(val):
    """
    преобразовывает арабское число в римское
    :param val:
    :return roman_str:
    """
    roman_str = ''
    for arabic_number, rome_number in reversed(arab_rome.items()):
        # прохождение по элементам словаря с конца, чтобы считать наиближайшее к арабскому числу ключ
        # например, к 1133 ближайший ключ - 1000
        while val >= arabic_number:
            roman_str += rome_number
            val -= arabic_number
    return roman_str
# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [1133, 2224, 1938, 1817, 2505, 391, 3743, 1634, 699, 1666, 1494, 1444]

test_data = [
    "MCXXXIII", "MMCCXXIV", "MCMXXXVIII", "MDCCCXVII", "MMDV", "CCCXCI", 'MMMDCCXLIII', 'MDCXXXIV', 'DCXCIX', 'MDCLXVI',
    'MCDXCIV', 'MCDXLIV']


for i, d in enumerate(data):
    assert to_roman(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
