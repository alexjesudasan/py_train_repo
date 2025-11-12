# Write a function to print a message
# def message():
#     print("Welcome to Python Functions")
# def greet():
#     print("Have a good day !")
# for i in range(2):
#     message()
# greet()

#==========================
#function with default args
# def add_numbers( a = 7,  b = 8):
#     sum = a + b
#     print('Sum:', sum)
#
# # function call with two arguments
# add_numbers(2, 3)
# #  function call with one argument
# add_numbers(a = 2)
# # function call with no arguments
# add_numbers()

#==========================
#function keyword args
# def display_info(first_name, last_name):
#     print('First Name:', first_name)
#     print('Last Name:', last_name)
#
# display_info(last_name = 'Jesudasan', first_name = 'Alex')
#==========================
#function with arbitrory args
#program to find sum of multiple numbers
# def find_sum(*numbers):
#     result = 0
#     for num in numbers:
#         result = result + num
#     print("Sum = ", result)
#
# # function call with 3 arguments
# find_sum(1, 2, 3)
# # function call with 2 arguments
# find_sum(4, 9)
#==========================
#function with positional args
# def nameAge(name, age):
#     print("Hi, I am", name)
#     print("My age is ", age)
#
#
# # You will get correct output because
# # argument is given in order
# print("Case-1:")
# nameAge("Suraj", 27)
# # You will get incorrect output because
# # argument is not in order
# print("\nCase-2:")
# nameAge(27, "Suraj")

#==============
# # def buy_vegetables():
#     carrot = 2
#     return carrot
#
# a = buy_vegetables()
# print("Bought" ,a , "vegetables")

#local variables
# def checklocal():
#     a=5
#     return (a+5)
#
# a=30
# val=checklocal()
# print(val)
# print(a)

# #Write a function with global variable
# a=5 #global variable
# def incrby5():
#     global a  #using global in local func
#     a+=5
#     return a
# def incrby10(b):
#     b+=10
#     return b
# b=23
# print(incrby5()) # output 10
# print(a) #output global a as 10
# print(incrby10(b)) #outputs 33
# print(b) #outputs 23

#Function taking parameters
# def message(l):
#     print("Hello " + l + ", Good Morning!!")
#
# l1 = ['David', 'Raju', 'Samson']
# for i in range(len(l1)):
#     message(l1[i])

#Function returning an integer
# def add(a,b):
#     c=a+b
#     return c
# x=y=5
# z=add(x,y)
# print(z)

#Function returning a string
# def greet(time):
#     if (time<12):
#         return "Good morning"
#     else:
#         return "Good Day"
#
# msg=greet (7)
# print(msg)
# msg=greet (14)
# print(msg)

#Returning more than 1 variables in func
# def addsub(a,b):
#     return a+b,a-b
#
# p=addsub(4,2)
# print(p)
# x,y= (addsub(9,6))
# print(x,y)
# Positional arguments
# def add(x, y):
#   return x + y
# result = add(5, 3)
#
# # Keyword arguments
# def greet(name, message="Hello"):
#   print(message + ", " + name)
# greet(name="Alice", message="Hi")
# greet("Bob") # Uses default message
#
# # Default arguments
# def power(base, exponent=2):
#     return base ** exponent
# result = power(5) # Uses default exponent of 2
# result = power(5, 3) # Overrides default exponent
#
# # Arbitrary arguments
# def sum_all(*numbers):
#   total = 0
#   for num in numbers:
#     total += num
#   return total
# result = sum_all(1, 2, 3, 4)
#
# #=== passing variable length of arguments
# def func1(*var):
#     print(var)
#     print(var[0]+20)
#
# func1(10)
# func1(50, 30, 20)
#
#
#
#
# # Nested calls
# def f1():
#     print('Inside f1()')
#     f2()
#
# def f2():
#     print('Inside f2()')
#
# f1()
#
# #Recursion
# def fact(f):
#     if f<=1:
#         return 1
#     return f*fact(f-1)
#
# p=fact(3)
# print(p)
#
#Lambda function
# y=lambda x:x*2
#
# print(y(5))


#calling lambda inside a function
# def doub(a):
#     return lambda n:n*a
#
# d=doub(5)
# print(d(3))


# for i in reversed(l):
#     print(i)
# for i in l[::-1]:
#     print(i)
# for i in range(len(l),2,-1):
#     print(i)
# l=[1,2,2,1]
# p=list(reversed(l))
# if p == l:
#     print("yes")
# else:
#     print("no")

# num = int(input("Enter a number: "))
# original = num
# reversed_num = 0
#
# # First for loop to count number of digits
# count = 0
# temp = num
# for i in str(temp):
#     count += 1
#
# # Second for loop to reverse the number
# temp = num
# for i in range(count):
#     digit = temp % 10
#     reversed_num = reversed_num * 10 + digit
#     print("reversed num =", reversed_num, "temp =", temp)
#     temp //= 10
#
# # Check if the number is a palindrome
# if original == reversed_num:
#     print("Palindrome")
# else:
#     print("Not a palindrome")
# n=1234
# mylist=[]
# p=n
# while(p):
#     mylist.append(p%10)
#     p=p//10
# print(mylist)
# print(list(reversed(mylist)))

# double = lambda x: x * 2
# triple = lambda x: x * 3
#
# print(double(5))
# print(triple(5))



def ascend(n):
    return sorted(n)

list=[8,3,7,2,1]
print(ascend(list))
