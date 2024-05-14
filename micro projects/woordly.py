import random


def random_word():
    with open('russian.txt', 'r', encoding='utf-8') as f:
        return random.choice(f.readlines()).replace('\n', '').replace('ё', 'e')


def print_keyboard(unavailable_letters=[]):
    keyboard = ['йцукенгшщзхъ', 'фывапролджэ', 'ячсмитьбю']
    for index, line in enumerate(keyboard):
        print(' ' * index, end='')
        for letter in line:
            if letter in unavailable_letters:
                letter = '_'
            print(letter, end=' ')
        print()


def main():
    print_keyboard()


if __name__ == '__main__':
    main()
