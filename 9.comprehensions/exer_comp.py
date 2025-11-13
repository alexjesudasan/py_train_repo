#1Convert the items in INR
# old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}
# new_price ={key:val*85 for key,val in old_price.items()}
# print(new_price)

#2Given a list of words, return a list containing only the words longer than 3 characters.
# words = ["hi", "apple", "dog", "banana"]
# new_words=[x for x in words if len(x)>3]
# print(new_words)

#3)Given a list of numbers, return a new list containing the factorial of each number
#formula n!=n*(n-1)!
# import math
# nums = [1, 2, 3, 4]
# fact = [math.factorial(x) for x in nums]
# print (fact)

#4)Given a string, extract all digits and return them as integers in a list.
# s = "abc123xyz4"
# s1= [x for x in s if x.isdigit()]
# print(s1)

#5)Given a list of strings, remove all empty or whitespace-only strings.
# strings = ["apple", "", " ", "banana", "grape"]
# clean_strings=[x for x in strings if x.isalpha()]
# print(clean_strings)

#6)Generate a 2D list (matrix) that represents a multiplication table from 1 to n
# n=3
# output =[[i * j for j in range(1, n+1)] for i in range(1, n+1)]
# print(output)
# count=0
# for lst in output:
#     count+=1
#     i=1
#     for num in lst:
#         print(f"{count}x {i}={num}")
#         i+=1


# #7)Given a 2D list (list of lists), return a flattened list containing all the elements.
input=[[1, 2], [3, 4], [5]]
list1=list2=[]
# for i in input:
#     for j in i:
#         list1.append(j)
# print(list1)
list2=[j for i in input ]
print(list2)