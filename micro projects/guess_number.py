import random
import simple_colors

def is_valid_num(number: int):
    if 1 <= number <= num:
        return True
    return False

def is_valid_word(result: str):
    result = result.lower()
    if result in ['да', 'нет']:
        return True
    else:
        return False

def repeatable_input():
    global number
    number = int(input((simple_colors.yellow('Введите число: '))))
    while is_valid_num(number) == False:
        number = int(input(simple_colors.red(f'А может быть все-таки введем число в диапазоне от 1 до {num}?: ')))

def setting_value(result: str):
    global num
    while is_valid_word(result) == False:
        print(simple_colors.red('Я тебя непонял повтори'))
        result = input(simple_colors.yellow('Хочешь изменить диапазон чисел для угадывания? (да/нет): ')).lower()
    if result == 'да':
        num = int(input(simple_colors.yellow('Тогда, введи число: ')))
        return num
    elif result == 'нет':
        num = 100
        return num
        
def game():
    tries = 0
    print(simple_colors.magenta('Добро пожаловать в числовую угадайку \nПо умолчанию диапазон чисел от 1 до 100'))
    result = input(simple_colors.yellow('Хочешь изменить диапазон чисел для угадывания? (да/нет): ')).lower()
    setting_value(result)
    required_number = random.randint(1, num)
    print()
    print(simple_colors.magenta('Игра началась!'))
    repeatable_input()
    tries += 1
    while number != required_number:
        if number > required_number:
            print(simple_colors.cyan('Твоё число больше загаданного, попробуй еще разок'))
        elif number < required_number:
            print(simple_colors.blue('Твоё число меньше загаданного, попробуй еще разок'))
        tries += 1
        repeatable_input()
    print(simple_colors.magenta(f'\x1B[1;3mПобеда!\x1B[0m \n\x1B[3mКоличество попыток: {tries}.\x1B[0m'))

def restart():
    result = input(simple_colors.yellow('Хочешь еще раз?: '))
    while is_valid_word(result) == False:
        print(simple_colors.red('Я тебя непонял, повтори'))
        result = input(simple_colors.yellow('Хочешь еще раз?: '))
    if result == 'да':
        game()
    else:
        print(simple_colors.magenta('\x1B[1;3mУдачи!\x1B[0m ') + simple_colors.magenta('\x1B[3mУвидимся\x1B[0m ') + simple_colors.magenta('\x1B[1mв другой раз.\x1B[0m'))

game()
restart()