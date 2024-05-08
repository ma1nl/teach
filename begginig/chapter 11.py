# num, word = int(input()), ''
# for i in range(num):
#     word += chr(97 + i)
# mylist = list(word)
# print(mylist)

# numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
# print(min(numbers) + max(numbers))

# numbers = [4, 2]
# numbers.extend([1, 2, 3])
# numbers.extend([7, 17, 777])
# print(numbers)

# n = int(input())
# words = []
# for i in range(n):
#     words.append(input())
# print(words)

# words =[]
# for i in range(26):
#     letter = chr(97 + i) * (i + 1)
#     words.append(letter)
# print(words)

# n = int(input())
# numbers = []
# for i in range(n):
#     number = int(input())
#     number = number ** 3
#     numbers.append(number)
# print(numbers)

# n = int(input())
# numbers = []
# for i in range(1, n + 1):
#     if n % i == 0:
#         numbers.append(i)
# print(numbers)

# rotate, numb, s_numbers = int(input()), 0, []
# for i in range(rotate):
#     number = int(input())
#     if numb == 0:
#         numb = number
#     else:
#         numb += number
#         s_numbers.append(numb)
#         numb = number
# print(s_numbers)

# rotate, list_numb = int(input()), []
# for i in range(rotate):
#     list_numb.append(int(input()))
# del list_numb[1::2]
# print(list_numb)

# n, list_word = int(input()), []
# for i in range(n):
#     message = input()
#     list_word.append(message)
# k = int(input())
# for j in range(len(list_word)):
#     m = list_word[j]
#     if len(m) >= k:
#         print(m[k - 1], end="")

# abc = ['abcd', 'abvg', 'bcde']
# print(abc[1][2])

# n, list_w = int(input()), []
# for i in range(n):
#     list_w.extend(input())
# print(list_w)

# numbers, number = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111], 0
# for i in range(len(numbers)):
#     number += (numbers[i] ** 2)
# print(number)

# n, list_numb = int(input()), []
# for i in range(n):
#     list_numb.append(int(input()))
# print(*list_numb, sep='\n')
# print()
# for i in range(len(list_numb)):
#     func = (list_numb[i] ** 2) + (2 * list_numb[i]) + 1
#     print(func)

# n, list_num = int(input()), []
# for _ in range(n):
#     list_num.append(int(input()))
# minimum = list_num.index(min(list_num))
# del list_num[minimum]
# maximum = list_num.index(max(list_num))
# del list_num[maximum]
# print(*list_num, sep='\n')

# n, list_w = int(input()), []
# for i in range(n):
#     w = input()
#     if w not in list_w:
#         list_w.append(w)
# print(*list_w, sep='\n')

# n, list_w = int(input()), []
# for _ in range(n):
#     list_w.append(input())
# search_w = input()
# search_w = search_w.lower()
# for message in list_w:
#     null = message.lower()
#     if null.find(search_w) > -1:
#         print(message)

# n, list_words = int(input()), []
# for _ in range(n):
#     list_words.append(input())
# k, list_search_words = int(input()), []
# for _ in range(k):
#     list_search_words.append(input())
# final_list = []
# for i in range(len(list_words)):
#     count = 0
#     for j in range(len(list_search_words)):
#         if list_search_words[j].lower() in list_words[i].lower():
#             count += 1
#     if count == len(list_search_words):
#         final_list.append(list_words[i])
# print(*final_list, sep='\n')

# n, list_numbers = int(input()), []
# for _ in range(n):
#     list_numbers.append(int(input()))
# sort_list = []
# for num in list_numbers:
#     if num < 0:
#         sort_list.append(num)
# for num in list_numbers:
#     if num == 0:
#         sort_list.append(num)
# for num in list_numbers:
#     if num > 0:
#         sort_list.append(num)
# print(*sort_list, sep='\n')

# n = input().split()
# print('\n'.join(n))

# n = input()
# n = ' '.join(n)
# n = n.split()
# up_word = []
# for i in range(len(n)):
#     if n[i] in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЭЮЯ':
#         up_word.append(n[i])
# print('.'.join(up_word), '.', sep='')

# n = input().split('\\')
# print('\n'.join(n))

# n = input().split()
# for i in range(len(n)):
#     print('+' * int(n[i]))

# n, count = input().split('.'), 0
# for i in range(len(n)):
#     if 0 <= int(n[i]) <= 255:
#         count += 1
# if count == 4:
#     print('ДА')
# else:
#     print('НЕТ')

# text = input().split(' ')
# text = ' '.join(text)
# divide = input()
# print(divide.join(text))

# n, count = input().split(), 0
# for i in range(len(n)):
#     for j in range(i):
#         if int(n[i]) == int(n[j]):
#             count += 1
# print(count)

# n, int_numb = input().split(), []
# if len(n) > 1:
#     for i in range(len(n)):
#         int_numb.append(int(n[i]))
#     min_num = min(int_numb)
#     max_num = max(int_numb)
#     position_min = int_numb.index(min_num)
#     position_max = int_numb.index(max_num)
#     int_numb.remove(min_num)
#     int_numb.remove(max_num)
#     int_numb.insert(position_min, max_num)
#     int_numb.insert(position_max, min_num)
# else:
#     for i in range(len(n)):
#         int_numb.append(int(n[i]))
#         int_numb.append(0)
#     min_num = min(int_numb)
#     max_num = max(int_numb)
#     position_min = int_numb.index(min_num)
#     position_max = int_numb.index(max_num)
#     int_numb.remove(min_num)
#     int_numb.remove(max_num)
#     int_numb.insert(position_min, max_num)
#     int_numb.insert(position_max, min_num)
#     int_numb.remove(0)
# print(*int_numb)

# n = input()
# n = n.lower()
# n = n.split()
# cnt_a = n.count('a')
# cnt_an = n.count('an')
# cnt_the = n.count('the')
# print('Общее количество артиклей:', cnt_a + cnt_an + cnt_the)

# n = input()
# n = " ".join(n)
# n = n.split()
# n.remove('#')
# n = ''.join(n)
# for _ in range(int(n)):
#     string = input()
#     if string.find('#') == -1:
#         string.rstrip()
#         print(string)
#     else:
#         string = string[:string.find('#')]
#         string = string.rstrip()
#         print(string)

# list_num = []
# for num in input().split():
#     list_num.append(int(num))
# list_num.sort()
# print(*list_num)
# list_num.sort(reverse=True)
# print(*list_num)

# palindromes = [m for m in range(100, 1001) if str(m) == str(m)[::-1]]
# print(palindromes)

# square = [n**2 for n in range(1, int(input()) + 1)]
# print(*square, sep='\n')

# string = input().split()
# cube = [int(string[i]) ** 3 for i in range(len(string))]
# print(*cube)

# print(*[i for i in input().split()], sep="\n")

# print(*[i for i in input() if i in '0123456789'], sep='')

# print(*[int(i)**2 for i in input().split() if int(i) % 2 == 0 and (int(i)**2) % 10 != 4])

# a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
# n = len(a)
# for i in range(1, n):
#     elem = a[i]  # берем первый элемент из неотсортированной части списка
#     j = i

#     # пока элемент слева существует и больше нашего текущего элемента
#     while j >= 1 and a[j - 1] > elem:
#         # смещаем j-й элемент отсортированной части вправо
#         a[j] = a[j - 1]
#         # сами идём влево, дальше ищем место для нашего текущего элемента
#         j -= 1

#     # нашли место для нащего текущего элемента из неотсортированной части
#     # и вставляем его на индекс j в отсортированной части
#     a[j] = elem
# print('Отсортированный список:', a)

# print([i for i in range(2, int(input()) + 1, 2)])

# l = [int(i) for i in input().split()]
# m = [int(i) for i in input().split()]
# lm = []
# for i in range(len(l)):
#     lm.append(l[i] + m[i])
# print(*lm)

# list_num = input().split()
# sum_num = sum([int(i) for i in list_num])
# print('+'.join(list_num), '=', sum_num, sep='')

# num_phone = input()
# only_digit_phone = num_phone.replace('-', '')
# cnt = 0
# if only_digit_phone.isdigit() == True:
#     cnt += 1
# if num_phone.count('-') == 2:
#     if len(num_phone) == 12 and num_phone[3] == '-' and num_phone[7] == '-':
#         cnt += 1
# elif num_phone.count('-') == 3:
# if num_phone[0] == '7'
# and len(num_phone) == 14
# and num_phone[1] == '-'
# and num_phone[5] == '-'
# and num_phone[9] == '-':
#         cnt += 1
# if cnt == 2:
#     print('YES')
# else:
#     print('NO')

# string = input().split()
# bigger = 0
# for word in string:
#     if len(word) >= bigger:
#         bigger = len(word)
# print(bigger)

print(*[word[1:] + word[0] + 'ки' for word in input().split()])
