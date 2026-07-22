#2 Given a string, count the number of vowels (a, e, i, o, u).
# name="alex"
# vowels=['a','e','i','0','u']
# sum=0
# for i in name:
#     if i in vowels:
#         sum+=1
# print(f"The number of vowels in {name} is: {sum}")    

#3 -Write a program to reverse a given string 
# name="alex"
# print(f"Reverse of string {name} is {name[::-1]}")
      
#4Count how many uppercase and lowercase letters are present.
# name="Chosen IT Academy"
# upper=lower=0
# for ch in name:
#     if ch.isupper():
#         upper+=1
#     elif ch.islower():
#         lower+=1
# print(f"Number of uppercase chars: {upper} and lowercase chars: {lower}")

#5Count how many times a given character appears in a string.
# my_str=input("Enter the string :")
# letter=input("Enter the character :")
# count=0
# for ch in my_str:
#     if ch == letter:
#         count+=1
# print(f"The count of character {letter} in {my_str} is {count}")        

#6Check  the given string  is a palindrome  or not. A palindrome reads the same forwards and backwards. (For eg. madam, mom)
# my_str=input("Enter the string :")
# rev_str=my_str[::-1]
# if rev_str == my_str:
#     print(f"The given string {my_str} is a palindrome")
# else:
#      print(f"The given string {my_str} is not a palindrome")

#7Count how many words are present in a sentence.
# my_line=input("Enter the line :")
# word=1
# for ch in my_line:
#     if ch == " ":
#         word+=1
# print(f"The number of words is {word}")

#8Find the Longest Word in a Sentence 
# my_line=input("Enter the line :")
# words=my_line.split()
# longest=" "
# for word in words:
#     if len(word)>len(longest):
#         longest=word
# print(f"The longest word is :{longest}")

#9Check if Two Strings End with the Same Three Character
# s1=input("Enter first string :")
# s2=input("Enter second string :")
# if s1.endswith("w") and s2.endswith("w"):
#     print("Yes the strings ends with w")
# else:
#     print("No the strings ends not with w")

#10Check if One String is the Reverse of another (eg. live and evil)
s1=input("Enter first string :")
s2=input("Enter second string :")
if s1 == s2[::-1]:
    print("Yes the strings are the reverse of the other")
else:
    print("No the strings are not the reverse of other")