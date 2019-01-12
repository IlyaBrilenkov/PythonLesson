one = ord(input('Введите английскую букву'))
two = ord(input('Введите другую английскую букву '))

place_one = one - 96
place_two = two - 96

if place_one == place_two:
    print(f'Введена одна буква, порядковый номер: {place_one}')
else:
    distance = abs(one - two) - 1
    print(f'порядковый номер первой буквы: {place_one}, порядковый номер второй буквы: {place_two}, букв между ними: {distance}')
