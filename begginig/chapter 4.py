# # Напишите программу, которая считывает три числа и подсчитывает количество чётных чисел.
# num1, num2, num3 = int(input()), int(input()), int(input())
# counter = 0  # переменная счётчик
# if num1 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# if num2 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# if num3 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# print(counter)

# pass1, pass2 = input(), input()
# if pass1 == pass2:
#     print('Пароль принят')
# else:
#     print('Пароль не принят')

# num = int(input())
# if num % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')

# num = int(input())
# fourth = num % 10
# third = num // 10 % 10
# second = num // 100 % 10
# first = num // 1000 % 10
# if first+fourth == second-third:
#     print('ДА')
# else:
#     print('НЕТ')

# num = input()
# if int(num[0])+int(num[3]) == int(num[1])-int(num[2]):
#     print('ДА')
# else:
#     print('НЕТ')

# age = int(input())
# if age >= 18:
#     print('Доступ разрешен')
# else:
#     print('Доступ запрещен')

# first, second, third = int(input()), int(input()), int(input())
# if second == first + (third-second) and third == first + 2*(third-second):
#     print('YES')
# else:
#     print('NO')

# first, second, third, fourth = int(input()), int(input()), int(input()), int(input())
# if first < second:
#     second = first
# if second < third:
#     third = second
# if third < fourth:
#     print(third)
# else:
#     print(fourth)

# age = int(input())
# if age <= 13:
#     print('детство')
# if 14 <= age <= 24:
#     print('молодость')
# if 25 <= age <= 59:
#     print('зрелость')
# if 60 < age:
#     print('старость')

# first, second, third = int(input()), int(input()), int(input())
# if first <= 0:
#     first = 0
# if second<= 0:
#     second = 0
# if third <= 0:
#     third = 0
# print(first+second+third)

# a = int(input())
# if -1 < a < 17:
#     print('Принадлежит')
# else:
#     print('Не принедлежит')

# a = int(input())
# if a<=-3 or a>=7:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')

# a = int(input())
# if -30 < a <= -2 or 7 < a <= 25:
#     print("Принадлежит")
# else:
#     print("Не принадлежит")

# a = int(input())
# if a>999 and a<10000:
#     if a % 7 == 0 or a % 17 == 0:
#         print('YES')
#     else:
#         print('NO')
# else:
#     print('NO')

# a, b, c = int(input()), int(input()), int(input())
# if a+b>c and a+c>b and b+c>a:
#     print('YES')
# else:
#     print('NO')

# a = int(input())
# if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
#     print('YES')
# else:
#     print('NO')

# first_y, first_x, second_y, second_x = int(input()), int(input()), int(input()), int(input())
# if 1 <= first_x <= 8 and 1 <= first_y <= 8 and 1 <= second_x <= 8 and 1 <= second_y <= 8:
#     if second_y == first_y or second_x == first_x:
#         print('YES')
#     else:
#         print('NO')
# else:
#     print('NO')

# first_y, first_x, second_y, second_x = int(input()), int(input()), int(input()), int(input())
# if 1 <= first_x <= 8 and 1 <= first_y <= 8 and 1 <= second_x <= 8 and 1 <= second_y <= 8:
#     if first_y - 1 <= second_y <= first_y + 1 and first_x - 1 <= second_x <= first_x + 1:
#         print('YES')
#     else:
#         print('NO')
# else:
#     print('NO')

# flash, zoom = int(input()), int(input())
# if flash > zoom:
#     print('NO')
# elif flash < zoom:
#     print('YES')
# else:
#     print("Don't know")

# a, b, c = int(input()), int(input()), int(input())
# if a == b == c:
#     print('Равносторонний')
# elif a == b or b == c or a == c:
#     print('Равнобедренный')
# else:
#     print('Разносторонний')

# first, second, third = int(input()), int(input()), int(input())
# if second < first < third or third < first < second:
#     print (first)
# elif first < second < third or third < second < first:
#     print (second)
# elif first < third < second or second < third < first:
#     print (third)

# mounth = int(input())
# if (
#     mounth == 1
#     or mounth == 3
#     or mounth == 5
#     or mounth == 7
#     or mounth == 8
#     or mounth == 10
#     or mounth == 12
# ):
#     print(31)
# elif mounth == 4 or mounth == 6 or mounth == 9 or mounth == 11:
#     print(30)
# elif mounth == 2:
#     print(28)

# height = int(input())
# if height < 60:
#     print('Легкий вес')
# elif 60 <= height < 64:
#     print('Первый полусредний вес')
# elif 64 <= height < 69:
#     print('Полусредний вес')

# num_1, num_2, func = int(input()), int(input()), input()
# if func == '+':
#     print(num_1 + num_2)
# elif func == '-':
#     print(num_1 - num_2)
# elif func == '*':
#     print(num_1*num_2)
# elif func == '/':
#     if num_2 !=0:
#         print(num_1 / num_2)
#     else:
#         print('На ноль делить нельзя!')
# else:
#     print('Неверная операция')

# color_1, color_2, = input(), input()
# if (color_1 == 'красный' or color_1 == 'желтый') and (color_2 == 'красный' or color_2 == 'желтый'):
#     if color_1 == 'красный' and color_2 == 'желтый':
#         print('оранжевый')
#     elif color_1 == 'желтый' and color_2 == 'красный':
#         print('оранжевый')
#     elif color_1 == 'красный' and color_2 =='красный':
#         print('красный')
#     elif color_1 =='желтый' and color_2 =='желтый':
#         print('желтый')
# elif (color_1 == 'красный' or color_1 == 'синий') and (color_2 == 'красный' or color_2 == 'синий'):
#     if color_1 == 'красный' and color_2 == 'синий':
#         print('фиолетовый')
#     elif color_1 == 'синий' and color_2 == 'красный':
#         print('фиолетовый')
#     elif color_1 == 'красный' and color_2 =='красный':
#         print('красный')
#     elif color_1 =='синий' and color_2 =='синий':
#         print('синий')
# elif (color_1 == 'синий' or color_1 == 'желтый') and (color_2 == 'синий' or color_2 == 'желтый'):
#     if color_1 == 'синий' and color_2 == 'желтый':
#         print('зеленый')
#     elif color_1 == 'желтый' and color_2 == 'синий':
#         print('зеленый')
#     elif color_1 == 'синий' and color_2 =='синий':
#         print('синий')
#     elif color_1 =='желтый' and color_2 =='желтый':
#         print('желтый')
# else:
#     print('ошибка цвета')

# number = int(input())
# if number == 0:
#     print('зеленый')
# elif 1 <= number <= 10:
#     if number % 2 == 0:
#         print('черный')
#     else:
#         print('красный')
# elif 11 <= number <= 18:
#     if number % 2 == 0:
#         print('красный')
#     else:
#         print('черный')
# elif 19 <= number <= 28:
#     if number % 2 == 0:
#         print('черный')
#     else:
#         print('красный')
# elif 29 <= number <= 36:
#     if number % 2 == 0:
#         print('красный')
#     else:
#         print('черный')
# else:
#     print('ошибка ввода')

# a_1, a_2, b_1, b_2 = int(input()), int(input()), int(input()), int(input())
# if a_2 > b_1 and a_2 >= b_2 and a_1 <= b_1 and a_1 <= b_2 :
#     print(b_1, b_2)
# elif a_2 > b_1 and a_2 > b_2 and a_1 >= b_1 and a_1 < b_2:
#     print(a_1, b_2)
# elif a_2 > b_1 and a_2 <= b_2 and a_1 >= b_1:
#     print(a_1, a_2)
# elif a_2 > b_1 and a_2 <= b_2:
#     print(b_1, a_2)
# elif a_1 == b_1 or a_1 == b_2:
#     print(a_1)
# elif a_2 == b_1 or a_2 == b_2:
#     print (a_2)
# else:
#     print('пустое множество')

# year = int(input())
# if year % 100 == 0:
#     print('YES')
# else:
#     print('NO')

# first_x, first_y, second_x, second_y =int(input()), int(input()), int(input()), int(input())
# if first_x % 2 != 0 and first_y % 2 !=0 and second_x % 2 != 0 and second_y % 2 != 0:
#         print('YES')
# elif first_x % 2 == 0 and first_y % 2 == 0 and second_x % 2 == 0 and second_y % 2 == 0:
#         print('YES')
# elif first_x % 2 != 0 and first_y % 2 == 0 and second_x % 2 != 0 and second_y % 2 == 0:
#         print('YES')
# elif first_x % 2 == 0 and first_y % 2 != 0 and second_x % 2 == 0 and second_y % 2 != 0:
#         print('YES')
# elif first_x % 2 != 0 and first_y % 2 != 0 and second_x % 2 == 0 and second_y % 2 == 0:
#         print('YES')
# elif first_x % 2 == 0 and first_y % 2 == 0 and second_x % 2 != 0 and second_y % 2 != 0:
#         print('YES')
# elif first_x % 2 == 0 and first_y % 2 != 0 and second_x % 2 != 0 and second_y % 2 == 0:
#         print('YES')
# elif first_x % 2 != 0 and first_y % 2 == 0 and second_x % 2 == 0 and second_y % 2 != 0:
#         print('YES')
# else:
#     print('NO')

# age, male = int(input()), input()
# if 10 <= age <= 15 and male == 'f':
#     print('YES')
# else:
#     print('NO')

# numb = int(input())
# if numb == 1:
#     print('I')
# elif numb == 2:
#     print('II')
# elif numb == 3:
#     print('III')
# elif numb == 4:
#     print('IV')
# elif numb == 5:
#     print('V')
# elif numb == 6:
#     print('VI')
# elif numb == 7:
#     print('VII')
# elif numb == 8:
#     print('VIII')
# elif numb == 9:
#     print('IX')
# elif numb == 10:
#     print('X')
# else:
#     print('ошибка')

# numb = int(input())
# if numb % 2 != 0:
#     print('YES')
# elif numb % 2 == 0:
#     if  numb <= 5 or numb > 20:
#         print('NO')
#     else:
#         print ('YES')

# x_1, y_1, x_2, y_2 = int(input()), int(input()), int(input()), int(input())

# if (x_2-x_1)**2 == (y_2-y_1)**2:
#     print('YES')
# else:
#     print('NO')

# x_1, y_1, x_2, y_2 = int(input()), int(input()), int(input()), int(input())
# if (x_2 - x_1)**2 == 4 and (y_2 - y_1)**2 == 1:
#     print('YES')
# elif (x_2 - x_1)**2 == 1 and (y_2 - y_1)**2 == 4:
#     print('YES')
# else:
#     print('NO')

# x_1, y_1, x_2, y_2 = int(input()), int(input()), int(input()), int(input())
# if x_1 == x_2 or y_1 == y_2 or (x_2-x_1)**2 == (y_2-y_1)**2:
#     print('YES')
# else:
#     print('NO')