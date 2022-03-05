#1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

name = input('Name - ')
age = input('Age - ')
cat = input('Cat name - ')
with open ('5-1.txt', 'w') as f:
    data = f.write(f'Name - {name}\nAge - {age}\nCat name - {cat}\n')
