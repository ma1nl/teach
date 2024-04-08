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


def print_digit_sum(num: int):
    num = [int(i) for i in str(num)]
    summa = sum(num)
    print(summa)

n = int(input())
print_digit_sum(n)