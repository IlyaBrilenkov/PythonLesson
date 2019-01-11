number1 = int(input('Введите первое число'))
number2 = int(input('Введите второе число'))
number3 = int(input('Введите третье число'))

if number1 > number2:
    if number1 > number3:
        if number2 > number3:
            print(f'{number2} среднее число')
        else:
            print(f'{number3} среднее число')
    else:
        print(f'{number1} среднее число')
else:
    if number2 > number3:
        if number1 > number3:
            print(f'{number1} среднее число')
        else:
            print(f'{number3} среднее число')
    else:
        print(f'{number2} среднее число')