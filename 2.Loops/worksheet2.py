#1 Find the sum of a given number
# num=int(input("Enter a number :"))
# sum=0
# while(num>0):
#     sum+=num%10
#     num//=10
#     print(num, sum)
#2Find the sum of 1+22+33+…. N
# sum=0
# num=int(input("Enter a number :"))
# while(num>0):
#     sum+=num**num
#     num-=num
#     print(num, sum)
# print(sum)
#
# #3 Multiplication table
# num = int(input("Enter a number: "))
#
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")

#Accept 10 numbers from the user and print the average
sum=0
num = input("Enter 3 numbers: ").split(',')
for i in num:
    sum+=int(i)
print(f"average is {int(sum/len(num))}")
