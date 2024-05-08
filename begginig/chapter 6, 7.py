# for i in range(10):
#     print('Python is awesome!')

# letter, numb = input(), int(input())
# for i in range(numb):
#     print(letter)

# for i in range(6):
#     print('A'*3)
# for i in range(5):
#     print('B'*4)
# print('E')
# for i in range(9):
#     print('T'*5)
# print('G')

# n = int(input())
# for i in range(n):
#     print('*'*19)

# letter = input()
# for i in range(10):
#     print(i, letter)

# n = int(input())
# for i in range(n+1):
#     print('Квадрат числа', i, 'равен', i**2)

# n = int(input())
# for i in range(n, 0, -1):
#     print('*'*i)

# start_numb_org, medium_up, days = int(input()), int(input()), int(input())
# for i in range(days):
#     population = pow((1 + medium_up / 100), i) * start_numb_org
#     print(i + 1, population)

# m, n = int(input()), int(input())
# for i in range(m, n+1):
#     print(i)

# m, n = int(input()), int(input())
# if m < n:
#     for i in range(m, n + 1):
#         print(i)
# else:
#     for i in range(m, n - 1, -1):
#         print(i)

# m, n = int(input()), int(input())
# for i in range(m, n - 1, -1):
#     if i % 2 != 0:
#         print(i)

# m, n = int(input()), int(input())
# for i in range(m, n+1):
#     if i % 17 == 0:
#         print(i)
#     elif i % 10 == 9:
#         print(i)
#     elif i % 3 == 0 and i % 5 == 0:
#         print(i)

# n = int(input())
# for i in range(1, 11):
#     print(n, 'x', i, '=', n*i)

# num = int(input())
# flag = True

# for i in range(2, num):
#     if num % i == 0:  #  если исходное число делится на какое-либо отличное от 1 и самого себя
#         flag = False

# if num == 1:
#     print('Это единица, она не простая и не составная')
# elif flag == True:
#     print('Число простое')
# else:
#     print('Число составное')

# total = 0
# for i in range(1, 6):
#     total += i
#     print(total, end="")

# a, b = int(input()), int(input())
# counter = 0
# for i in range(a, b+1):
#     if i % 10 == 4 or i % 10 == 9:
#         counter += 1
# print(counter)

# n = int(input())
# total = 0
# for i in range(n):
#     numb = int(input())
#     total += numb
# print(total)

# import math
# n = int(input())
# total = 0
# for i in range(1, n+1):
#     numb = 1 / i
#     total += numb
# result = total - math.log(n)
# print(result)

# n = int(input())
# total = 0
# for i in range(1, n+1):
#     if i**2 % 10 == 2 or i**2 % 10 == 5 or i**2 % 10 == 8:
#         total += i
# print(total)

# n = int(input())
# total = 1
# for i in range (1, n + 1):
#     total *= i
# print(total)

# total = 1
# for i in range(10):
#     n = int(input())
#     if n != 0:
#         total *= n
# print(total)

# n = int(input())
# total = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         total += i
# print(total)

# n = int(input())
# total = 0
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         total -= i
#     else:
#         total += i
# print(total)

# n = int(input())
# total = 0
# numb_min = 0
# for i in range(n):
#     numb = int(input())
#     if numb_min < numb:
#         numb_min, numb = numb, numb_min
#         if numb_min > total:
#             numb_min, total = total, numb_min
# print(total, numb_min, sep="\n")

# flag = True
# for i in range(10):
#     n = int(input())
#     if n % 2 != 0:
#         flag = False
# if flag == True:
#     print('YES')
# elif flag == False:
#     print('NO')

# n = int(input())
# x = 1
# y = 0
# if n == 1:
#     print(n)
# elif n >= 2:
#     print(x, end = ' ')
#     for i in range(n-1):
#         total = y + x
#         print(total, end = ' ')
#         y, x = x , total

# text = input()
# total = 0
# while text != 'stop':
#     total += int(text)
#     text = input()
# print('Сумма чисел равна', total)

# text = input()
# while text != "КОНЕЦ":
#     print(text)
#     text = input()

# text = input()
# while text != 'КОНЕЦ' and text != 'конец':
#     print(text)
#     text = input()

# text = input()
# total = 0
# while text != 'стоп' and text != 'хватит' and text != 'достаточно':
#     total += 1
#     text = input()
# print(total)

# numb = int(input())
# while numb % 7 == 0:
#     print(numb)
#     numb = int(input())

# numb = int(input())
# total = 0
# while numb > -1:
#     total += numb
#     numb = int(input())
# print(total)

# numb = int(input())
# total = 0
# while 1 <= numb <= 5:
#     if numb == 5:
#         total += 1
#     numb = int(input())
# print(total)

# numb = int(input())
# coins = 0
# while numb >= 25:
#     coins += 1
#     numb -= 25
# while 25 > numb >= 10:
#     coins += 1
#     numb -= 10
# while 10 > numb >= 5:
#     coins += 1
#     numb -= 5
# while 0 < numb < 5:
#     coins += 1
#     numb -= 1
# print(coins)

# num = int(input())
# has_seven = False  # сигнальная метка
# while num != 0:
#     last_digit = num % 10
#     if last_digit == 7:
#         has_seven = True
#     num = num // 10
# if has_seven == True:
#     print('YES')
# else:
#     print('NO')

# numb = int(input())
# while numb != 0:
#     last_numb = numb % 10
#     print(last_numb, end = '')
#     numb //= 10

# numb = int(input())
# mx, mn = 0, 9
# while numb != 0:
#     x = numb % 10
#     y = numb % 10
#     if x > mx:
#         x, mx = mx, x
#     if y < mn:
#         y, mn = mn, y
#     numb //= 10
# print('Максимальная цифра равна', mx)
# print('Минимальная цифра равна', mn)

# numb = int(input())
# summa, kolv, mulplic, sr_arf, first_numb, sum_first_last = 0, 0, 1, 0, 0, 0
# last_numb = numb % 10
# while numb != 0:
#     x = numb % 10
#     summa += x
#     kolv += 1
#     mulplic *= x
#     if numb < 10:
#         first_numb = x
#     numb //= 10
# sr_arf = summa  / kolv
# sum_first_last = first_numb + last_numb
# print(summa, kolv, mulplic, sr_arf, first_numb, sum_first_last, sep='\n')

# numb = int(input())
# while numb != 0:
#     if 9 < numb < 100:
#         x = numb % 10
#     numb //= 10
# print(x)

# numb = int(input())
# flag = True
# a = numb % 10
# while numb != 0:
#     b = numb % 10
#     if a != b:
#         flag = False
#     numb //= 10
# if flag == False:
#     print('NO')
# else:
#     print('YES')

# numb = int(input())
# flag = True
# b = 0
# while numb != 0:
#     a = numb % 10
#     if b <= a:
#         a, b = b, a
#     else:
#         flag = False
#     numb //= 10
# if flag == False:
#     print('NO')
# else:
#     print('YES')

# i = 100
# while i > 0:
#     if i == 40:
#         break
#     print(i, end='*')
#     i -= 20

# n = 10
# while n > 0:
#     n -= 1
#     if n == 2:
#         continue
#     print(n, end='*')

# numb = int(input())
# flag = True
# for i in range(2, numb + 1):
#     if numb % i == 0:
#         flag = False
#         break
# print(i)

# numb = int(input())
# for i in range(1, numb + 1):
#     if 5 <= i <= 9:
#         continue
#     elif 17 <= i <= 37:
#         continue
#     elif 78 <= i <= 87:
#         continue
#     print(i)

# mx = -10**6
# s = 0
# for i in range(10):
#     x = int(input())
#     if x < 0:
#         s += x
#     if x > mx and x < 0:
#         mx = x
# if s < 0:
#     print(s)
#     print(mx)
# else:
#     print('NO')

# n = int(input())
# flag = False
# max_digit = 0
# while n > 0:
#     digit = n % 10
#     if digit % 3 == 0:
#         flag = True
#         if digit > max_digit:
#             max_digit = digit
#     n = n // 10
# if flag:
#     print(max_digit)
# else:
#     print('NO')

# n = int(input())
# while n > 0:
#     numb = n % 10
#     n //= 10
# print(numb)

# n = int(input())
# product = 1
# while n > 0:
#     digit = n % 10
#     product *= digit
#     n //= 10
# print(product)

# n = int(input())
# for i in range (n):
#     for j in range(3):
#         print(n, end = ' ')
#     print()

# n = int(input())
# for i in range(1, n + 1):
#     for j in range(5):
#         print(i, end=" ")
#     print()

# n = int(input())
# for i in range (1, n + 1):
#     for j in range(1, 10):
#         print(i, '+', j, '=', i + j)
#     print()

# from math import ceil
# n = int(input())
# mid = ceil(n / 2)
# while n >= mid:
#     for i in range(1, mid + 1):
#         print("*" * i, end="")
#         print()
#         n -= 1
# else:
#     for i in range(mid - 1, 0, -1):
#         print("*" * i, end="")
#         print()
#         n -= 1

# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(i, end="")
#     print()

# for n in range(1, 14):
#     for k in range (1, 13):
#         for m in range (1, 12):
#             if 28 * n + 30 * k + 31 * m == 365:
#                 print('n=', n, 'k=', k, 'm=', m)

# for b in range(1, 10):
#     for k in range(1, 20):
#         for t in range(1, 100):
#             if 10 * b + 5 * k + 0.5 * t == 100 and b + k + t == 100:
#                 print('b=', b, 'k=', k, 't=', t)

# for a in range(1, 150):
#     for b in range(a, 150):
#         for c in range(b, 150):
#             for d in range(c, 150):
#                 for e in range(d, 150):
#                     if a < b < c < d < e and a ** 5 + b ** 5 + c **5 + d ** 5 == e **5:
#                         print(a + b + c + d + e)

# n = int(input())
# k = 1
# for i in range(1, n + 1):
#     for j in range(i):
#         print(k, end=' ')
#         k += 1
#     print()

# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     for j in range(i - 1, 0, -1):
#         print(j, end="")
#     print()

# a, b = int(input()), int(input())
# max_del, sum_del, max_numb = 0, 0, 0
# for i in range(a, b + 1):
#     for j in range(1, i + 1):
#         if i % j == 0:
#             sum_del += j
#     if sum_del >= max_del:
#         max_del= sum_del
#         max_numb = i
#     sum_del = 0
# print(max_numb, max_del)

# n = int(input())
# for i in range(1, n + 1):
#     count = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             count += 1
#     print(i, "+" * count, sep="")

# n = int(input())
# while n > 9:
#     count = 0
#     while n > 0:
#         last_num = n % 10
#         count += last_num
#         n //= 10
#     n = count
# print(n)

# n = int(input())
# numb = 0
# for i in range(1, n + 1):
#     fact = 1
#     for j in range(1, i + 1):
#         fact *= j
#     numb += fact
# print(numb)

# a, b = int(input()), int(input())
# if a == 1:
#     a += 1
# for i in range(a, b + 1):
#     total = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             total += 1
#     if total < 3:
#         print (i)

# n = int(input())
# s = 0
# while n > 0:
#     if n % 2 == 0:
#         s += (n % 10)
#     n //= 10
# print(s)

# count = 0
# maximum = -10**12
# for i in range(8):
#     x = int(input())
#     if x % 4 == 0:
#         count += 1
#         if x > maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

# count = 0
# maximum = -10**8
# for i in range(4):
#     x = int(input())
#     if x % 2 != 0:
#         count += 1
#         if x > maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

# n = int(input())
# for i in range(1, n + 1):
#     if i == 1 or i == n:
#         print("*" * 19, sep="")
#     else:
#         print("*", " " * 17, "*", sep="")

# n = int(input())
# while n > 100:
#     numb = n % 10
#     n //= 10
# print(numb)

# n = int(input())
# last_numb = n % 10
# numb_3 = 0
# numb_ravnih = 0
# chetnye = 0
# summ_more_5 = 0
# count_more_7 = 1
# numb_5and0 = 0
# while n > 0:
#     last_digit = n % 10
#     if last_digit == 3:
#         numb_3 += 1
#     if last_numb == last_digit:
#         numb_ravnih += 1
#     if last_digit % 2 == 0:
#         chetnye += 1
#     if last_digit > 5:
#         summ_more_5 += last_digit
#     if last_digit > 7:
#         count_more_7 *= last_digit
#     if last_digit == 0 or last_digit == 5:
#         numb_5and0 += 1
#     n //= 10
# print(numb_3, numb_ravnih, chetnye, summ_more_5, count_more_7, numb_5and0, sep='\n', end='')
