# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input('Введите число '))
arrey = []

while num > 0:
    arrey.append(num % 2)
    num //= 2

for i in range((len(arrey) - 1), -1, -1):
    print(arrey[i], end = '')