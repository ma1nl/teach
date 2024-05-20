# weight, lenght = float(input()), float(input())
# imt = weight / (lenght * lenght)
# if 18.5 > imt:
#     print('Недостаточная масса')
# elif 18.5 <= imt <= 25:
#     print('Оптимальная масса')
# elif imt > 25:
#     print('Избыточная масса')

# string = input()
# l_string = len(string)
# total_cost = l_string * 60
# rubles = total_cost // 100
# pennies = total_cost % 100
# print(f'{rubles} р. {pennies} коп.')

# print(len([i for i in input().split()]))

# # year = int(input())
# animals = [
#     "Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца"
#     ]
# current_animal = year % 12
# print(animals[current_animal])
# number = input()
# if len(number) == 5 and number[-1] == '0':
#     number = number.replace('0', '')
#     number = number[-1:-6:-1]
# elif len(number) == 5:
#     number = number[-1:-6:-1]
# elif len(number) == 6:
#     number = number[0] + number[-1:-6:-1]
# print(number)

# number =int(input())
# print(f'{number:,}')

# number = list(input()[::-1])
# lenght = len(number)
# if len(number) > 5:
#     add = 0
#     for i in range(3, len(number), 3):
#         number.insert(i + add, ',')
#         add += 1
#     print(''.join(number[::-1]))
# if len(number) > 3 and len(number) < 6:
#     number.insert(3, ',')
#     print(''.join(number[::-1]))
# if len(number) < 4:
#     print(''.join(number[::-1]))

# iteration = int(input())
# cnt_1, cnt_2, cnt_3, cnt_4 = 0, 0, 0, 0
# list_xy = []
# for i in range(iteration):
#     xy = input().split()
#     list_xy.append(xy)
# for i in range(len(list_xy)):
#     if int(list_xy[i][0]) > 0 and int(list_xy[i][1]) > 0:
#         cnt_1 += 1
#     elif int(list_xy[i][0]) < 0 and int(list_xy[i][1]) > 0:
#         cnt_2 += 1
#     elif int(list_xy[i][0]) < 0 and int(list_xy[i][1]) < 0:
#         cnt_3 += 1
#     elif int(list_xy[i][0]) > 0 and int(list_xy[i][1]) < 0:
#         cnt_4 += 1
# print(f'Первая четверть: {cnt_1}\nВторая четверть: {cnt_2}\nТретья четверть: {cnt_3} \nЧетвертая четверть: {cnt_4}')

# numbers = input().split()
# cnt = 0
# for number in range(1, len(numbers)):
#     if int(numbers[number]) > int(numbers[number-1]):
#         cnt += 1
# print(cnt)

# list_numbers = input().split()
# for i in range(1, len(list_numbers), 2):
#     list_numbers[i], list_numbers[i-1] = list_numbers[i-1], list_numbers[i]
# print(*list_numbers)

# list_numbers = input().split()
# last_symbol = list_numbers.pop(-1)
# list_numbers.insert(0, last_symbol)
# print(*list_numbers)

# numbers = input().split()
# cnt = 1
# for number in range(1, len(numbers)):
#     if int(numbers[number]) != int(numbers[number-1]):
#         cnt += 1
# print(cnt)

# numbers, flag = [], False
# for i in range(int(input())):
#     numbers.append(int(input()))
# op = int(input())
# for i in range(len(numbers)):
#     for j in range(len(numbers)):
#         if i != j:
#             if numbers[i] * numbers[j] == op:
#                 flag = True
#                 break
# if flag:
#     print('ДА')
# else:
#     print('НЕТ')

# timur = input()
# ruslan = input()
# if timur == 'камень' and ruslan == 'ножницы':
#     print('Тимур')
# elif timur == 'ножницы' and ruslan == 'бумага':
#     print('Тимур')
# elif timur == 'бумага' and ruslan == 'камень':
#     print('Тимур')
# elif timur == 'камень' and ruslan == 'ящерица':
#     print('Тимур')
# elif timur == 'ящерица' and ruslan == 'Спок':
#     print('Тимур')
# elif timur == 'Спок' and ruslan == 'ножницы':
#     print('Тимур')
# elif timur == 'ножницы' and ruslan == 'ящерица':
#     print('Тимур')
# elif timur == 'ящерица' and ruslan == 'бумага':
#     print('Тимур')
# elif timur == 'бумага' and ruslan == 'Спок':
#     print('Тимур')
# elif timur == 'Спок' and ruslan == 'камень':
#     print('Тимур')
# elif timur == ruslan:
#     print('ничья')
# else:
#     print('Руслан')

# coin_flip = input().split('О')
# print(len(max(coin_flip)))

# alive = [i for i in range(1, int(input()) + 1)]
# step = int(input())
# killer_index = 0
# while len(alive) > 1:
#     victim_index = (killer_index + step - 1) % len(alive)
#     alive.pop(victim_index)
#     killer_index = victim_index % len(alive)
# print(*alive)

# words, list_indexs = [], []
# current_word = ['a', 'n', 't', 'o', 'n']
# step = 0
# len_current_word = len(current_word)
# for i in range(int(input())):
#     words.append(input())
# for word in words:
#     step += 1
#     cnt = 0
#     for letter in current_word:
#         i = word.find(letter)
#         word = word[i:]
#         if letter in word:
#             cnt += 1
#     if cnt == len_current_word:
#         list_indexs.append(step)
# print(*list_indexs)

# text = input() + ' запретил букву'
# list_letters = [chr(i) for i in range(ord('а'), ord('я') + 1)]
# for index_letter in range(len(list_letters)):
#     if list_letters[index_letter] in text:
#         print(f'{text} {list_letters[index_letter]}')
#         text = text.replace(list_letters[index_letter], '')
#         text = ' '.join(text.split())
