#4. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

rus_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('5-4rus.txt', 'w', encoding='utf-8') as fru:
    with open('5-4.txt', 'r', encoding='utf-8') as f:
        fru.write(str([line.replace(line.split()[0], rus_dict.get(line.split()[0])) for line in f]))