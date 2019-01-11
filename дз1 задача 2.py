a = 5
b = 6

f_and = bin(a&b)
f_or = bin(a|b)
f_not_or = bin(a^b)
f_left_a2 = bin(a<<2)
f_right_a2 = bin(a>>2)

# Перевод обратно в десятичную систему счисления

f_and = int(f_and, base=2)
f_or = int(f_or, base=2)
f_not_or = int(f_not_or, base=2)
f_left_a2 = int(f_left_a2, base=2)
f_right_a2 = int(f_right_a2, base=2)

print(f'логическое И 5 и 6 = {f_and}')
print(f'логическое ИЛИ 5 и 6 = {f_or}')
print(f'исключающее ИЛИ 5 и 6 = {f_not_or}')
print(f'побитовой сдвиг влево на 2 знака числа 5 = {f_left_a2}')
print(f'побитовой сдвиг вправо на 2 знака числа 5 = {f_right_a2}')