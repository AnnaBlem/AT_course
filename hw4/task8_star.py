# Задача со ЗВЁЗДОЧКОЙ. Решать НЕ обязательно.
# Программа получает на вход натуральное число num.
# Программа должна вывести другое натуральное число, удовлетворяющее условиям:
# Новое число должно отличаться от данного ровно одной цифрой
# Новое число должно столько же знаков как исходное
# Новое число должно делиться на 3
# Новое число должно быть максимально возможным из всех таких чисел
# Например (Ввод --> Вывод) :
#
# 379 --> 879
# 15 --> 75
# 4974 --> 7974


def max_division_by_3(num):
    first_digit = num
    count_digits = 1
    while first_digit > 9:  # цикл, вычисляющий первую цифру числа и кол-во цифр
        first_digit //= 10
        count_digits += 1
    new_num = - 1
    perfect_digit = 9  # т.к. нужно вычислить максимальное число с заданными ограничениями, вводится
    # цифра 9 - максимальная цифра, которая в цикле будет уменьшаться, пока не выполнятся условия ограничения
    current_digit = first_digit  # текущая цифра, на которой стоим в цикле (от первой до последней)
    g = 1  # бегунок для вычисления следующих current_digit в цикле
    while new_num % 3 != 0:
        if (current_digit != 9) and (current_digit < perfect_digit):
            diff_max_current = perfect_digit - current_digit
            new_num = num + diff_max_current * 10 ** (count_digits - g)  
            perfect_digit -= 1
        else:
            if count_digits != g:
                g += 1
                current_digit = (num // 10 ** (count_digits - g)) % 10
                perfect_digit = 9
            else:
                new_num = num - 3
    return new_num
# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ

data = [
    379, 810, 981, 4974, 996, 9000, 15, 0, 9881, 9984, 9876543210, 98795432109879543210, 9, 999
]

test_data = [
    879, 870, 987, 7974, 999, 9900, 75, 9, 9981, 9987, 9879543210, 98798432109879543210, 6, 996
]


for i, d in enumerate(data):
    assert max_division_by_3(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')