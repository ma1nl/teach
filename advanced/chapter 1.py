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

iteration = int(input())
cnt_1, cnt_2, cnt_3, cnt_4 = 0, 0, 0, 0
for i in range(iteration):
    xy = input().split()
    list_xy = xy.append()
for i in range(iteration):
    if int(list_xy[i][0]) > 0 and int(list_xy[i][1]) > 0:
        cnt_1 += 1
    elif int(list_xy[i][0]) < 0 and int(list_xy[i][1]) > 0:
        cnt_2 += 1
    elif int(list_xy[i][0]) < 0 and int(list_xy[i][1]) < 0:
        