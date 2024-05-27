# right_side = int(input())
# list_num = []
# for i in range(right_side):
#     sub_list = [int(i) for i in range(1, right_side + 1)]
#     list_num.append(sub_list)
# for i in range(right_side):
#     print(list_num[i])

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)

# list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
# sub_list = ['h', 'i', 'j']
# list1[2][1][2].extend(sub_list)
# print(list1)

# list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# maximum = 0
# for numbers in list1:
#     if max(numbers) > maximum:
#         maximum = max(numbers)
# print(maximum)

# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# for i in range(len(list1)):
#     list1[i].reverse()
# print(list1)

# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# total = 0
# counter = 0
# for sub_list in list1:
#     total += sum(sub_list)
#     counter +=len(sub_list)
# print(total / counter)

# right_side = int(input())
# list_num = []
# for i in range(1, right_side + 1):
#     sub_list = [int(k) for k in range(1, i + 1)]
#     list_num.append(sub_list)
# for i in range(right_side):
#     print(list_num[i])

# n = int(input())
# lst = [[1]]
# for i in range(1, n + 1):
#     row = [1] * (i + 1)
#     for j in range(i + 1):
#         if j != 0 and j != i:
#             row[j] = lst[i - 1][j - 1] + lst[i - 1][j]
#     lst.append(row)
# print(lst[-1])

# n = int(input())
# lst = [[1]]
# for i in range(1, n + 1):
#     row = [1] * (i + 1)
#     for j in range(i + 1):
#         if j != 0 and j != i:
#             row[j] = lst[i - 1][j - 1] + lst[i - 1][j]
#     lst.append(row)
# for row in lst[:-1]:
#     print(*row)

# text = input().split()
# lst_sblst = [[text[0]]]
# for i in range(1, len(text)):
#     if text[i] == text[i - 1]:
#         lst_sblst[-1].append(text[i])
#     else:
#         lst_sblst.append([text[i]])
# print(lst_sblst)
