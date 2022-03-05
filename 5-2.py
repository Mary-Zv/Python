#2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

with open('5-2.txt', 'r') as f:
    file = f.read()
    print(f'Содержимое файла: \n{file}\n')

with open('5-2.txt', 'r') as f:
    string = f.readlines()
    print(f'Количество строк в файле - {len(string)}')

with open('5-2.txt', 'r') as f:
    content = f.readlines()
    for el in range(len(content)):
        print(f'Количество символов на {el + 1} строке {len(content[el])}')

with open('5-2.txt', 'r') as f:
    word = f.read()
    word = word.split()
    print(f'Всего слов - {len(word)}')