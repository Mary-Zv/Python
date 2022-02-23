#2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

list_num = [1, 2, 3, 4, 5, 6, 7]

if len(list_num) % 2 == 0:
    i = 0
    while i < len(list_num):
        el = list_num[i]
        list_num[i] = list_num[i+1]
        list_num[i+1] = el
        i += 2
else:
    i = 0
    while i < len(list_num) - 1:
        el = list_num[i]
        list_num[i] = list_num[i + 1]
        list_num[i + 1] = el
        i += 2
print(list_num)