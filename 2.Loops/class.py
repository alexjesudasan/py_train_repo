# #1
# # if-else
# amount=100
# cart=[]
# banana=int(input("Enter the amount of half kg banana :"))
# if banana <50:
#     cart = "banana","apples"
# else:
#     cart = "banana", "guava"
# print("Your cart has  :", cart) 
# input("Press Enter to continue to next...")

# #2
# #if-elif-else
# amount=100
# apples="no" #based on the yes or no you will buy choclates
# car=[]
# banana=int(input("Enter the amount of half kg banana :"))
# if banana >50:
#     cart = "banana","guava"
# elif apples =="yes":
#     cart = "banana", "apples"
# else:
#     cart = "banana","choclates"
# print("Your cart has  :", cart) 
# input("Press Enter to continue to next...")

# #3
# # if-elif-else
# # Create a Grading system based on the total marks %
# marks = int(input("Enter your marks %: "))
# if marks >= 90:
#     print("Grade: A")
# elif marks >= 75:
#     print("Grade: B")
# elif marks >= 50:
#     print("Grade: C")
# else:
#     print("Grade: Fail")
# print("End of program")
# input("Press Enter to continue to next...")

#4
# #print numbers using for-loop
# for i in range(-10, 5,2):
#     print(i)

# #5
# #printing your name letter by letter
# name=input("Enter your name :")
# for letter in name:
#     print(letter)

# #6
# #printing members in list
# fruits =["banana","apples","orange"]
# for i in fruits:
#     print(i)

# #7
# #multiplication table
# for i in range(1, 11):
#     print("5 x", i, "=", 5 * i)

# #9
# #sum of set of numbers
# total=0
# for i in range(10):
#     total=total+i
# print(total)

# #10
# #while loop
# i = 1
# while i <= 5:
#     print(i)
#     i += 1

#11
n=10
result = []
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        result.append("FizzBuzz")
    elif i % 3 == 0:
        result.append("Fizz")
    elif i % 5 == 0:
        result.append("Buzz")
    else:
        result.append(str(i))
print (result)