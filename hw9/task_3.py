
# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код


sum_list = []
sum_of_purchase = 0
with open('test_file/task_3.txt', encoding='utf-8') as file:
    for line in file:
        if line != '\n':
            sum_of_purchase += int(line)
        else:
            sum_list.append(sum_of_purchase)
            sum_of_purchase = 0
sum_list.sort(reverse=True)
three_most_expensive_purchases = sum(sum_list[0:3])
assert three_most_expensive_purchases == 202346
