import random

print('сгенирируем целое число в заданном диапазоне')
m1 = int(input('Введите первое число:'))
m2 = int(input('Введите второе число:'))
n = int(random.random() * (m2 - m1 + 1)) + m1
print(n)

print('сгенирируем вещественное число в заданном диапазоне')
m1 = float(input('Введите первое число:'))
m2 = float(input('Введите второе число:'))
n = random.random() * (m2 - m1) + m1
print(round(n, 3))

print('сгенирируем символ в заданном диапазоне')
m1 = ord(input('Введите первый символ:'))
m2 = ord(input('Введите второй символ:'))
n = int(random.random() * (m2 - m1 + 1)) + m1
print(chr(n))
