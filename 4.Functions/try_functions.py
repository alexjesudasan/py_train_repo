# x = 5
# def foo():
# 	global x
# 	y = "local"
# 	x = x * 2
# 	print(x)
# 	print(y)
#
# print("Global variable", x)
# foo()
# print("global variable now", x)
# def factorial(number):
#     if number == 1:
#         # BASE CASE
#         return 1
#     else:
#         # RECURSIVE CASE
#         return number * factorial(number - 1)
# print(factorial(5))

# #Anagram program
#
# magic=123
# def check_numb_digits(n):
#     s1=str(n)
#     if len(s1) >=3:
#         return 0 #fail
#     return 1
#
# def check_numb_miss(n):
#     s1=str(magic)
#     s2=str(n)
#     for i in s1:
#         if i not in s2:
#             return 0  #fail
#     return 1
#
# def check_numb_dup(n):
#     s1=str(magic)
#     s2=str(n)
#     count=0
#     for i in s1: #123
#         for j in s2: #121
#             if (i==j):
#                 count+=1
#                 if count>1:
#                     print("count =", count)
#                     print("number has duplicate digits")
#                     return 0 #fail
#         count =0
#     return 1
#
# def conv_to_list(n):
#     p=n
#     l1=[]
#     while(p):
#         l1.append(int(p%10))
#         p=p//10
#     l2=list(reversed(l1))
#     return l2
#
#
# n=int(input("Enter a number :"))
# validate1=check_numb_digits(n)
# validate2=check_numb_dup(n)
# validate3=check_numb_miss(n)
# # print (validate1,validate2,validate3)
# if not validate1 and not validate2 and not validate3 :
#     print ("Enter a valid number, should not have missing or duplicate digits")
#     exit()
#
#
# l2=conv_to_list(n)
# for i in l2:
#     if (str(i) not in str(magic)):
#         anag_flag="not an anagram"
#     else:
#         anag_flag='anagram'
# if (anag_flag == 'anagram'):
#     print ('The given number is an anagram of 123')
# else:
#     print('The given number is not an anagram of 123')

# Palindrome program
# n=int(input("Enter a number :"))
# s1=str(n)
# half=int(len(s1)/2)
# l1= (s1[:half])
# l2= (s1[half:])
## print(l1, l2)
# for i in l1:
#     if i!= l2[n-1]:
#         print(' not a palindrome')
#         exit()
#     else:
#         n=n-1
# print ('palindrome')

#palindrome with recursion


def palindrom(s1):
    global s2,leng
    '''palindrome function'''
    print(len(s1), int(leng/2))
    if (len(s1) < int(leng/2)):
        if (s1[0] == s1[-1]):
            print ("palindrome")
        else:
            print("not a palindrome")
        return
    else:
        if (s1[0] == s1[-1]):
            # print("digit is same")
            s2 =(s1[1:-1])
            palindrom(s2)
        else:
            print("not palindrome")
            return None

n=int(input("Enter a number :"))
s1=str(n)
print(palindrom.__doc__)
s2=[]
leng=int(len(s1))
palindrom(s1)


# for i in l1:
#     if i!= l2[n-1]:
#         print(' not a palindrome')
#         exit()
#     else:
#         n=n-1
# print ('palindrome')