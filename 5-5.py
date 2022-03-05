#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

from random import randint

with open('5-5.txt', mode='w+', encoding='utf-8') as f:
    f.write(' '.join([str(randint(1, 100)) for _ in range(1000)]))
    f.seek(0)
    print(sum(map(int, f.readline().split())))