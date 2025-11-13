dictionary = {
    k1: {k2: k1 * k2 for k2 in range(1, 6)} for k1 in range(2, 5)
}
print(dictionary)

# numbers = range(10)
# ages =[35,15,8,2]
# # even_numbers = [x for x in numbers if x % 2 == 0]
# child_adult =['adult' if age >21 else 'child' for age in ages]
# print(child_adult)