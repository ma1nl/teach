import random


class Word:
    def __init__(self, file_path) -> None:
        self.words = self._load_words_from(file_path)

    def _load_words_from(self, file_path: str) -> list:
        with open(file_path, 'r', encoding='utf-8') as f:
            return [word.replace('\n', '').replace('ё', 'е') for word in f.readlines()]

    def get_random_word(self) -> str:
        return random.choice(self.words)

    def exists(self, word: str) -> bool:
        left_bound = 0
        right_bound = len(self.words) - 1
        while left_bound <= right_bound:
            middle = (right_bound + left_bound) // 2
            if word == self.words[middle]:
                return True
            elif word > self.words[middle]:
                left_bound = middle + 1
            else:
                right_bound = middle - 1
        return False


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
    words = Word('russian.txt')
    word_to_find = words.get_random_word()
    left_word = 'ааааа'
    right_word = 'яяяяя'
    while True:
        word = input().lower()
        if words.exists(word):
            if word > word_to_find:
                if word < right_word:
                    right_word = word
                print(left_word + '..' + right_word)
            elif word < word_to_find:
                if word > left_word:
                    left_word = word
                print(left_word + '..' + right_word)
            else:
                print('vse')
                break
        else:
            print('Ne suschestvuet')


if __name__ == '__main__':
    main()
