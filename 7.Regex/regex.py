# import re
# #Common functions
# #Search
# text="Python3.83"
# match = re.search("\d+\.\d+", text)
# if match:
#     print("Match found : ", match.group())
# else:
#     print("Match not found")
# #findall
# print (re.findall("\d+", "My Birthday is 30th April 4th Month 1991"))
# print(re.findall ("^G", "Good Morning Good Night"))
# #split
# print (re.split("\d+", "My Birthday is 30th April 4th Month 1991"))
# #substitute with another word
# print (re.sub("My Birthday", "His Wedding Day", "My Birthday is 30th April 4th Month 1991"))

#Quantifiers
# #* means zero or more accurances
# print (re.findall("ab*", "abc abb axy abab"))
# print (re.findall("ab*", "ac axy"))
# #+ means one or more accurances
# print (re.findall("ab+", "abc abb axy"))
# print (re.findall("ab+", "ac axy"))
# #? means preceding char either present or absent
# print (re.findall("b?ombay", "bbombay ombay bombay"))
# #{} matches n accurances of the preceeding char
# print (re.findall("go{2}d", "good goud gooood"))
# #{} matches  accurances n to m of the preceeding char
# print (re.findall("go{2,4}d", "good goud gooood"))

#Metacharacters
# strings=['Thine is the kingdom', "Abba Father"]
# for string in strings:
#     if (re.match('^T',string)):
#         print("matched string is :", string)
#     else:
#         print("no match string  :", string)

# #Sequences
# text = "The price is Rs123.45, and the date is 2025-06-27."
# # Find all digits
# digits = re.findall(r'\d+', text)
# print("Digits:", digits)
#
#
# #Sets

import re
email='jesudasan.alexander@gmail.com'
email1='john.doe@gmail.com'
# match_vowel = re.findall('[aeiouAEIOU]', email)
# name=re.match('jesudasan', email)
name=re.findall(r'[\w\.]+',email1)
# print("Vowels found:", match_vowel)
print (name)