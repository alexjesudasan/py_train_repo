# Tail Recursion method - Work and is done before the recursive call
# and nothing to do when it returns
# def reverse_number(num, rev=0):
#     global count
#     count += 1
#     print(f"call count :{count},{num},{rev}")
#     if num == 0:
#         print (f"reverse num : {rev}")
#         return rev
#     #work is done first
#     digit = num % 10
#     rev = rev * 10 + digit
#     return reverse_number(num // 10, rev)
# count = 0
# num = int(input("Enter a number: "))
# print("Reversed number:", reverse_number(num))

#Head Recursion method - Recursive call happens first and the work is done
#as the stack unwinds
def reverse_number(num):
    global count
    count += 1
    print(f"call count :{count},{num}")
    if num == 0:
        print (f"reverse num : {num}")
        return num
    #recursive call happens first
    small_rev = reverse_number(num // 10)

    # Work done after recursion returns
    count -= 1
    print(f"call count :{count},{num}")
    digits = len(str(num))
    return (num % 10) * (10 ** (digits - 1)) + small_rev

count = 0
num = int(input("Enter a 4 digit number: "))
print("Reversed number:", reverse_number(num))


