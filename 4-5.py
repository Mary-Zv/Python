#5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.
#Подсказка: использовать функцию reduce().

from functools import reduce


def my_list(el, elem):
    return el * elem

new_list = [el for el in range(99, 1001) if el % 2 == 0]
print(f'лист\n{new_list}\nУмножение\n{reduce(my_list, new_list)}')