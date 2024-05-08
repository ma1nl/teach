# s = 'abcdef'
# for i in range(len(s)):
#     print(s[i], end=' ')
# print()
# for c in s:
#     print(c, end=' ')

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# if ',' in s:
#     print(s)

# c = input()
# for s in range(0, len(c), 2):
#     print(c[s])

# c = input()
# for s in range(len(c) - 1, -1, -1):
#     print(c[s])

# first_name, last_name, third_name = input(), input(), input()
# print(last_name[0], first_name[0], third_name[0], sep='')

# n = input()
# total = 0
# for i in range(len(n)):
#     numb = int(n[i])
#     total += numb
# print(total)

# n = input()
# flag = True
# if (
#     "0" in n
#     or "1" in n
#     or "2" in n
#     or "3" in n
#     or "4" in n
#     or "5" in n
#     or "6" in n
#     or "7" in n
#     or "8" in n
#     or "9" in n
# ):
#     flag = False
# if flag == True:
#     print("Цифр нет")
# else:
#     print("Цифра")

# n = input()
# total_plus = 0
# total_multiplic = 0
# for i in range(len(n)):
#     if n[i] in '+':
#         total_plus += 1
#     if n[i] in '*':
#         total_multiplic += 1
# print('Символ + встречается', total_plus, 'раз')
# print('Символ * встречается', total_multiplic, 'раз')

# n = input()
# total = 0
# for i in range(len(n)-1):
#     if n[i] == n[i+1]:
#         total += 1
# print(total)

# n = input()
# total_g, total_s = 0, 0
# for i in range(len(n)):
#     if n[i] in 'ауоыиэяюеАУОЫИЭЯЮЕ':
#         total_g += 1
#     elif n[i] in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
#         total_s += 1
# print('Количество гласных букв равно', total_g)
# print('Количество согласных букв равно', total_s)

# n = int(input())
# numb = ''
# while n > 0:
#     numb += str(n % 2)
#     n //= 2
# for i in range(len(numb)- 1, -1, -1):
#     print(numb[i], end="")

# n = input()
# if n[:] == n[::-1]:
#     print('YES')
# else:
#     print('NO')

# n = input()
# print(len(n))
# print(n * 3)
# print(n[0])
# print(n[:3])
# print(n[-3:])
# print(n[::-1])
# print(n[1:-1])

# n = input()
# print(n[2])
# print(n[-2])
# print(n[:5])
# print(n[:-2])
# print(n[::2])
# print(n[1::2])
# print(n[::-1])
# print(n[::-2])

# from math import ceil
# n = input()
# half_lenght = ceil(int(len(n)) / 2)
# print(n[half_lenght:] + n[:half_lenght])

# text = input()
# right_text = text.title()
# if text == right_text:
#     print('YES')
# else:
#     print('NO')

# text = input()
# text = text.swapcase()
# print(text)

# text = input()
# text = text.lower()
# good = "хорош"
# if good in text:
#     print("YES")
# else:
#     print("NO")

# text = input()
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# total = 0
# for i in range(len(text)):
#     if text[i] in alphabet:
#         total += 1
# print(total)

# s = 'foo bar foo baz foo qux'
# print(s.rfind('foo'))
# print(s.rfind('bar'))
# print(s.rfind('qu'))
# print(s.rfind('python'))

# n = input()
# space = n.count(' ')
# print(space + 1)

# n = input()
# n = n.lower()
# adein = n.count('а')
# guanin = n.count('г')
# citozin = n.count('ц')
# timin = n.count('т')
# print('Аденин:', adein)
# print('Гуанин:', guanin)
# print('Цитозин:', citozin)
# print('Тимин:', timin)

# n = int(input())
# total = 0
# for i in range(n):
#     text = input()
#     if text.count('11') >= 3:
#         total += 1
# print(total)

# n = input()
# n = n.replace(' ', '')
# numbers = 0
# for i in range(10):
#     numbers += n.count(str(i))
# print(numbers)

# n = input()
# if n.endswith('.com') == True or n.endswith('.ru') == True:
#     print('YES')
# else:
#     print('NO')

# text = input()
# total = 0
# word = ''
# for i in text:
#     if text.count(str(i)) >= total:
#         number = text.count(str(i))
#         total = number
#         word = i
# print(word)

# n = input()
# quantitty_f = n.count('f')
# if quantitty_f == 1:
#     print(n.find('f'))
# elif quantitty_f > 1:
#     print(n.find('f'), n.rfind('f'))
# elif quantitty_f == 0:
#     print('NO')

# text = input()
# first_h, last_h = text.find('h'), text.rfind('h')
# slc = text[first_h: last_h + 1]
# print(text.replace(slc, ''))

# first, last = int(input()), int(input())
# for i in range(first, last + 1):
#     print(chr(i), end=" ")

# n = input()
# for i in n:
#     print(ord(i), end=' ')

# n, text = int(input()), input()
# for i in text:
#     if ord(i) - n < 97:
#         raznica = n - (ord(i) - 97)
#         print(chr(123 - raznica), end="")
#     elif ord(i) - n > 96:
#         print(chr(ord(i) - n), end="")

# n = input()
# for i in range(len(n)):
#     if i % 3 != 0:
#         print(n[i], end="")

# n = input()
# print(n.replace('@', ''))

# n = input()
# total = 0
# for i in range(len(n)):
#     if n[i] == "f":
#         total += 1
#         if total > 1:
#             break
# if total > 1:
#     print(i)
# elif total == 1:
#     print(-1)
# else:
#     print(-2)

# text = input()
# first_h, last_h = text.find("h"), text.rfind("h")
# slc = text[first_h : last_h]
# slc = slc[::-1]
# print(text[:first_h + 1] + slc + text[last_h + 1:])

# n = input()
# n1 = n[1:]
# cnt = 0
# if n[0] == "@" and (5 <= len(n) <= 15):
#     cnt += 1
# if n1.isalnum() == True  and n.islower() == True:
#     cnt += 1
# elif n1.isalpha() == True and n.islower() == True:
#     cnt += 1
# elif n1.isdigit() == True:
#     cnt += 1
# if cnt == 2:
#     print("Correct")
# else:
#     print("Incorrect")

# num = int(input())
# for i in range(1, num + 1):
#     string = input()
#     if string.isspace() == True or string == '':
#         print(f"{i}: COMMENT SHOULD BE DELETED")
#     else:
#         print(f"{i}: {string}")

# number = input()
# letters = "АВЕКМНОРСТУХ"
# number_letters = number[0] + number[4:6]
# cnt = 0
# digit = number[-1:6:-1]
# if number[6] == '_':
#     cnt += 1
# if 9 <= len(number) <= 10:
#     cnt += 1
# if digit.isdigit():
#     cnt += 1
# for letter in number_letters:
#     if letter in letters:
#         cnt += 1
# if cnt == 6:
#     print('YES')
# else:
#     print('NO')

# day = int(input())
# weight = float(input())
# current_weight = 100 - (day * 0.2)
# if weight <= current_weight:
#     print('Все идет по плану')
#     print(f'#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {current_weight} кг')
# else:
#     print('Что-то пошло не так')
#     print(f'#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {current_weight} кг')
