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


# def merge_list(num_string: int):
#     global_string = []

#     for _ in range(num_string):

#         temporary_list = [int(j) for j in input().split()]

#     return global_string

# num = int(input())
# print(merge_list(num))


print(1)