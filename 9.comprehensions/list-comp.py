# vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for sublist in vector:
#     for item in sublist:
# #         print(item)
# vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# L = [number for sublist in vector for number in sublist]
# print(L)


#
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print (table)
for row in table:
    print(row)


# original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
# new_dict_1 = {k: ('old' if v > 40 else 'young')
#     for (k, v) in original_dict.items()}
# print(new_dict_1)
