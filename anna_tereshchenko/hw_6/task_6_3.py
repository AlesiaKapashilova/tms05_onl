def calculation(option, x, y):
    if option == 1:
        return print(f'Результат сложения = {x + y}')
    elif option == 2:
        return print(f'Результат вычитания = {x - y}')
    elif option == 3:
        return print(f'Результат умножения = {x * y}')
    elif option == 4:
        if x % y == 0:
            return print(f'Результат деления = {x / y}')
        else:
            return print(f'{x / y}\nЧастное: {x // y}, Остаток: {x % y}')


class IncorrectValue(Exception):
    pass


while True:
    try:
        option_input = int(input('1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\nВведите номер пункта меню:\n'))
        if option_input < 1 or option_input > 4:
            raise IncorrectValue
    except IncorrectValue:
        print('Введите число от 1 до 4: ')
        continue
    except ValueError:
        print('Это не число, пожалуйста, введите число: ')
        continue
    break

first_number = ''

while True:
    try:
        if not first_number:
            first_number = int(input('Введите первое число: '))
        second_number = int(input('Введите второе число: '))
        if option_input == 4 and second_number == 0:
            raise ZeroDivisionError
    except ZeroDivisionError:
        print('Делитель не может быть 0, пожалуйста, введите другое число')
        continue
    except ValueError:
        print('Это не число')
        continue
    break

res = calculation(option_input, first_number, second_number)
