# 1) Given a list, count how many int, float, str, and bool are present
# Lt=[10, 3.14, "hello", True, False, 42, "world", 2.5]
from unittest import case

# Lt=[10, 3.14, "hello", True, False, 42, "world", 2.5]
# d1={}
# for item in Lt:
#     t=type(item).__name__
#     d1[t]=1
#     if t in d1.keys():
#         d1[t]+=1
# print(d1)

# 2)Write a program to find whether a number is odd or even using bitwise AND
# a=int(input("Enter a number to check :"))
# if a&1==1:
#     print("odd number")
# else:
#     print("even number")

# 3)Create a simple calculator with 2 variables for doing basic arithmetic operations
# using the switch case statement
# a,b=2,3
# opr=input("Enter the operation +, _, / :")
# match opr:
#     case  "+":
#         print(a+b)
#     case "-":
#         print(a-b)
#     case "*":
#         print(a*b)
#     case "/":
#         print(a//b)
#     case _:
#         print("Invalid Operation")

# 4)Write a function that takes another function as argument and applies it.
# def func (func,val):
#     return func(val)
#
# def func2(value):
#     return (value)
#
# print(func(func2,5))

# 5)Write a function that counts lines, words, and characters in a file.
# lcount,wcount,ccount=0,0,0
# with open("test.txt") as f:
#     lines = f.readlines()
#     for line in lines:
#         lcount +=1
#         for word in line.split():
#             wcount+=1
#             for char in word:
#                 ccount+=1
# print("Line count is",lcount)
# print("Word count is",wcount)
# print("Character count is",ccount)

# 6)Write a program to merge contents of two text files into a third file.
# with open("story-1.txt","r")as f1:
#     text1=f1.read()
# with open("story-2.txt", "r") as f2:
#     text2 = f2.read()
# with open("story.txt", "w") as f3:
#     f3.write(text1)
#     f3.write(text2)
# print("The file story.txt has been created with contents of 2 files")

# 7)Check if a number is palindrome using while
# a=12432421
# palind=True
# while a>9:
#     b = (10 ** (len(str(a)) - 1))
#     if int(a/b) == a%10: #checking first and last digit
#         pass
#     else:
#         palind = False
#         break
#     c=b*(a%10)
#     a=int((a-c)/10)
#     print(a)
# if palind == True:
#     print ('Palindrome')
# else:
#     print('Not a Palindrome')

# 8)Find the sum of the elements in the list [4,7,12,3]
# l=[4,7,12,3]
# sum=0
# for i in l:
#     sum=sum+i
# print(sum)

# 9)Try entering a total of 5 student details in a dictionary.
# Assume you are breaking by saving 3 students and resuming it
# from the state where you left.
# (use pickle/unpickling)

# import pickle
# num=[]
# stud=[{},{},{}]
# for i in range(3):
#     stud[i]["name"]=input("Enter the student name :")
#     stud[i]["dob"]=input("Enter the DOB :")
# with open("student.pkl","wb") as f:
#     pickle.dump(stud,f)
#
# with open("student.pkl","rb") as f:
#     c=pickle.load(f)
# print(c)

# 10)Write a program that checks if a word exists in a file
with open('story.txt', 'r') as f:
    content = f.read()
    if "alex" in content:
        print("The word exists in the file")
    else:
        print("The word does not exist")