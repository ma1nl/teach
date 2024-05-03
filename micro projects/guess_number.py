import random
import simple_colors

def repeatable_input(num: int) -> int:
    '''Пока введенное число не будет находится в диапазоне чисел, будет просить ввести число'''
    number = input((simple_colors.yellow('Введите число: ')))
    while not is_valid_num(number, num):
        number = input(simple_colors.red(f'А может быть все-таки введем число в диапазоне от 1 до {num}?: '))
    return int(number)

def is_valid_num(number: str, num: int) -> bool:
    '''Если введенном числе нету символов и букв возращает True или False'''
    number = number.replace(' ', '')
    if number.isdigit() or number.isdecimal() == False:
        return 1 <= int(number) <= num

def is_valid_word(result: str) -> bool:
    '''Проверяет, корректно ли введено слово'''
    result = result.lower().replace(' ', '')
    return result in ['да', 'нет']

def change_guess_range(result: str) -> int:
    '''Позволяет изменить диапазон числа для угадывания'''
    while not is_valid_word(result):
        print(simple_colors.red('Я тебя непонял повтори'))
        result = input(simple_colors.yellow('Хочешь изменить диапазон чисел для угадывания? (да/нет): ')).lower().replace(' ', '')
    if result == 'да':
        num = input(simple_colors.yellow('Тогда, введи число: '))
        while not num.isdigit():
            num = input(simple_colors.yellow('Введи целочисленное число: '))
        return int(num)
    elif result == 'нет':
        return 100
        
def game():
    tries = 0
    print(simple_colors.magenta('Добро пожаловать в числовую угадайку \nПо умолчанию диапазон чисел от 1 до 100'))
    result = input(simple_colors.yellow('Хочешь изменить диапазон чисел для угадывания? (да/нет): ')).lower().replace(' ', '')
    num = change_guess_range(result)
    required_number = random.randint(1, num)
    print()
    print(simple_colors.magenta('Игра началась!'))
    number = repeatable_input(num)
    tries += 1
    while number != required_number:
        if number > required_number:
            print(simple_colors.cyan('Твоё число больше загаданного, попробуй еще разок'))
        elif number < required_number:
            print(simple_colors.blue('Твоё число меньше загаданного, попробуй еще разок'))
        tries += 1
        number = repeatable_input(num)
    print(simple_colors.magenta(f'\x1B[1;3mПобеда!\x1B[0m \n\x1B[3mКоличество попыток: {tries}.\x1B[0m'))

def restart():
    result = input(simple_colors.yellow('Хочешь еще раз?: '))
    while not is_valid_word(result):
        print(simple_colors.red('Я тебя непонял, повтори'))
        result = input(simple_colors.yellow('Хочешь еще раз?: '))
    if is_valid_word() and result == 'да':
        game()
    else:
        print(simple_colors.magenta('\x1B[1;3mУдачи!\x1B[0m ') + simple_colors.magenta('\x1B[3mУвидимся\x1B[0m ') + simple_colors.magenta('\x1B[1mв другой раз.\x1B[0m'))

game()
restart()