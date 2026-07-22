#Aim of this program to print the numbers in descending order using recursion
# count=0  # to track the number of times func is called
# def print_descend(n):
#     global count
#     count +=1
#     if n==0: #base case
#         count=0
#         return
#     print(f"call count ={count} n= {n}")
#     print_descend(n-1) #recursive case
#     #location where return stmt start executing
#     count+=1
#     print(f"return count ={count} n={n}")
#     return
#
# n=5
# print_descend(n)





# def print_even_digits(n):
#     # Base case
#     print(f"func called; n=  {n}")
#     if n == 0:
#         return
#
#     # Recursive call first (to process digits left to right)
#     print_even_digits(n // 10)
#
#     # Process last digit
#     print(f"after return; n= {n}")
#     digit = n % 10
#     if digit % 2 == 0:
#         print(f"Even Digit: {digit}")
#     return
#     print_even_digits(n // 10)
#
# num = 4825
# print_even_digits(num)

#To demo tail recursion
# def tail_sum(n, total=0):
#     if n == 0:
#         return total
#     return tail_sum(n - 1, total + n)
# print(tail_sum(5))

#To demo direct recursion
def countdown(n):
    if n == 0:
        print("Blast off!")
    else:
        print(n)
        countdown(n - 1)  # Direct call

countdown(3)