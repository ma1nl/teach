# def draw_box():
#     print('*'*10)
#     for i in range(12):
#         print(f"*{' ' * 8}*")
#     print('*'*10)

# draw_box()


# def draw_triangle():
#     print(*['*' * i for i in range(1, 11)], sep='\n')

# draw_triangle()


# def print_fio(name, surname, patronymic):
#     list_FIO = [surname, name, patronymic]
#     print(list_FIO[0][0].upper(), list_FIO[1][0].upper(), list_FIO[2][0].upper(), sep='')

# name, surname, patronymic = input(), input(), input()
# print_fio(name, surname, patronymic)


# def print_digit_sum(num: int):
#     num = [int(i) for i in str(num)]
#     summa = sum(num)
#     print(summa)

# n = int(input())
# print_digit_sum(n)


# def find_all(target: str, symbol):
#     index_current_symbol = []
#     for i in range(len(target)):
#         if target[i] == symbol:
#             index_current_symbol.append(i)
#     return index_current_symbol

# s = input()
# char = input()
# print(find_all(s, char))


# def merge(list1, list2):
#     global_list = list1 + list2
#     global_list.sort()
#     return global_list

# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]
# print(merge(numbers1, numbers2))


# def quick_merge(list1, list2):
#     result = []
#     p1 = 0
#     p2 = 0
#     while p1 < len(list1) and p2 < len(list2):
#         if list1[p1] <= list2[p2]:
#             result.append(list1[p1])
#             p1 += 1
#         else:
#             result.append(list2[p2])
#             p2 += 1
#     if p1 < len(list1):
#         result += list1[p1:]
#     else:
#         result += list2[p2:]

#     return result

# total_list = []
# for i in range(int(input())):
#     num = [int(q) for q in input().split()]
#     total_list = quick_merge(total_list, num)
# print(*total_list)


# def is_prime(num):
#     cnt = 0
#     for i in range(1, int(num) + 1):
#         if int(num) % i == 0:
#             cnt +=1
#     if cnt == 2:
#         return True
#     else:
#         return False

# n = int(input())
# print(is_prime(n))


# def get_next_prime(num):
#     num += 1
#     while is_prime(num) != True:
#         num += 1
#     return num

# n = int(input())
# print(get_next_prime(n))


# def is_password_good(password: str):
#     if len(password) < 8:
#         return False
#     cnt_n, cnt_l, cnt_b = 0, 0, 0
#     for i in range(len(password)):
#         if password[i].islower():
#             cnt_l += 1
#         if password[i].isupper():
#             cnt_b += 1
#         if password[i].isdigit():
#             cnt_n +=1
#     if cnt_b < 1 or cnt_l < 1 or cnt_n < 1:
#         return False
#     return True

# txt = input()
# print(is_password_good(txt))


# def is_one_away(word1, word2):
#     if len(word1) != len(word2):
#         return False
#     cnt_dif = 0
#     for i in range(len(word1)):
#         if word1[i] != word2[i]:
#             cnt_dif += 1
#     if cnt_dif != 1:
#         return False
#     return True

# txt1 = input()
# txt2 = input()
# print(is_one_away(txt1, txt2))


# def is_palindrome(text):
#     text = [i.lower() for i in text if i.isalpha()]
#     text = ''.join(text)
#     if text == text[::-1]:
#         return True
#     else:
#         return False

# txt = input()
# print(is_palindrome(txt))


# def is_valid_password(password: str):
#     if password.count(':') != 2:
#         return False
#     password = password.split(':')
#     if password[0] != password[0][::-1]:
#         return False
#     if is_prime(password[1]) == False:
#         return False
#     if int(password[2]) % 2 != 0:
#         return False
#     return True

# psw = input()
# print(is_valid_password(psw))


# def is_correct_bracket(text: str):
#     if text.find(')') == 0:
#         return False
#     cnt = 0
#     for i in range(len(text)):
#         if text[i] == '(':
#             cnt += 1
#         elif text[i] == ')':
#             cnt -= 1
#         if cnt < 0:
#             return False
#     if cnt == 0 and text[-1] == ')':
#         return True
#     else:
#         return False

# txt = input()
# print(is_correct_bracket(txt))


# def convert_to_python_case(text: str):
#     letters = []
#     letters.extend(text)
#     i = 1
#     while i < len(letters):
#         if letters[i].isupper():
#             letters.insert(i, '_')
#             i += 2
#         else:
#             i += 1
#     text = ''.join(letters).lower()
#     return text

# txt = input()
# print(convert_to_python_case(txt))


# def get_middle_point(x1, y1, x2, y2):
#     x = (x1 + x2) / 2
#     y = (y1 + y2) / 2
#     return x, y

# x_1, y_1 = int(input()), int(input())
# x_2, y_2 = int(input()), int(input())
# x, y = get_middle_point(x_1, y_1, x_2, y_2)
# print(x, y)


# from math import pi
# def get_circle(radius):
#     length = 2 * pi * radius
#     square = pi * (radius ** 2)
#     return length, square

# r = float(input())
# length, square = get_circle(r)
# print(length, square)


# from math import sqrt
# def solve(a, b, c):
#     D = b ** 2 - (4 * a * c)
#     if D > 0:
#         x1 = (-b + sqrt(D)) / (2 * a)
#         x2 = (-b - sqrt(D)) / (2 * a)
#         if x1 > x2:
#             return x2, x1
#         else:
#             return x1, x2
#     elif D == 0:
#         x = -(b / (2 * a))
#         return x, x

# a, b, c = int(input()), int(input()), int(input())
# x1, x2 = solve(a, b, c)
# print(x1, x2)


# def draw_triangle():
#     for i in range(1, 9):
#         print(' ' * (8 - i) + '*' * (i + (i - 1)), sep='')

# draw_triangle()


# def get_shipping_cost(quantity):
#     if quantity > 1:
#         return 1000 + ((quantity - 1) * 120)
#     else:
#         return 1000

# n = int(input())
# print(get_shipping_cost(n))


# from math import factorial
# def compute_binom(n, k):
#     result = int(factorial(n)) / int(factorial(k) * factorial(n - k))
#     return int(result)

# n = int(input())
# k = int(input())
# print(compute_binom(n, k))


# def number_to_words(num):
#     dig = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
#     dec = ['',  'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят',
#     'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
#     teen = ['', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать',
#         'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
#     if num < 10:
#         return dig[num]
#     elif 10 < num < 20:
#         return teen[num - 10]
#     elif num == 10 or 19 < num < 100:
#         digits = [int(i) for i in str(num)]
#         if digits[1] == 0:
#             number = dec[digits[0]]
#             return number
#         else:
#             number = [dec[digits[0]], dig[digits[1]]]
#             number = ' '.join(number)
#             return number

# n = int(input())
# print(number_to_words(n))


# def get_month(language, number):
# lng_ru = [
# 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь'
#     ]
# lng_en = [
# 'january', 'februar', 'march', 'april', 'may', 'june', 'jul', 'august', 'september', 'october', 'november', 'december'
#     ]

#     if language == 'ru':
#         return lng_ru[number - 1]
#     elif language == 'en':
#         return lng_en[number - 1]

# lan = input()
# num = int(input())
# print(get_month(lan, num))


# def is_magic(date: str):
#     date = date.split('.')
#     if int(date[0]) * int(date[1]) == int(date[2][2:4]):
#         return True
#     else:
#         return False

# date = input()
# print(is_magic(date))


# def is_pangram(text: str):
# letters = [
# 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
# ]
#     text = text.split()
#     text = ''.join(text)
#     for i in letters:
#         if i not in text.lower():
#             return False
#     return True

# text = input()
# print(is_pangram(text))
