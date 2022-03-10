#2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyError(Exception):
    def __init__(self, text):
        self.txt = text
num_1 = int(input("Введите делимое - "))
num_2 = int(input("Введите делитель - "))
try:
    if num_2 != 0:
        raise MyError(num_1 / num_2)
except ValueError:
    print("ашибачка")
except MyError as mr:
    print(mr)
else:
    print('ашибачка. на ноль нельзя')