
# for i in range(50,10,-2):
#     print("My name is Alex", i)

#for loop
# rows = 5
# for i in range(1, rows+1):
#     print("*" * i)

# # #while loop
# count = 5
# print("Count down starts")
# while count > 0:
#     print(f"{count} minutes" )
#     count -= 1

# n=int(input("Enter the number :")
# for i in range(1,n+1,2):
#     print(" " * (n-i)//2 + n*i)
# for i in range(1,n-1,2):
#     print(" " * (n-i)//2 + n*i)

name=input("Enter your name: ")
print(len(name))
for i in range(len(name)):
    print(name[i])
print("Reversing it")
for i in range(-1,-(len(name)+1),-1):
    print(name[i])