#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = input('Введите целое число n - ')

nn = str(n + n)
nnn = str(n + n + n)

print(int(n) + int(nn) + int(nnn))