print("\n^^^^^^^^^^^^^^Worksheet 1 Solutions^^^^^^^^^^^^^^\n")
# 1)If one Canadian dollar can be bought for INR 64.01, how much INR is required
# to buy 500 CAD?
print("------Problem 1------------")
cad=64.01
# n=int(input("Enter the CAD amount :"))
n=500
Total_INR=cad*n
print(Total_INR)


# 2)Assign values for principal (P), rate of interest (R), and time (T in years).
# Calculate the Simple Interest (SI = (P × R × T) / 100) and print the result.
print("------Problem 2------------")
P=1000
R=9.5
T=5
SI= P*R*T
print("SI")
# 3)Given an integer 1234, reverse its digits without converting it to a string
# and print the result as 4321
print("------Problem 3------------")
a=6745
print("Given number :",a)
d1=a//1000 #d1= 1
# print(d1)

a=a-(1000*d1)  #a=234
d2=a//100 #d2 =2
# print(d2)

a=a-(100*d2) # a=34
d3=a//10 #d3=3
# print(d3)

a=a-(10*d3) # a=4
d4=a
# print(d4)
# print(d4,d3,d2,d1)
print(d4*1000 + d3*100 + d2*10 + d1)

# 4)Multiply any given number by 2 without using multiplication operator.(hint -
# use left shift operator)
print("------Problem 4------------")
n=100
print(n>>1)
# 5)Check if the given  number is having two 1 bits
# Input: 6
# Output: Yes
# Input: 3
# Output: No
print("------Problem 5------------")
num=10
# temp= num & 2 or num & 5 or number & 6 or number 9 and number & 10 and number & 12
temp= num & 1
print(temp == 1)
num>>=1
temp= num & 1
print(temp == 1)
num>>=1
temp= num & 1
print(temp == 1)
num>>=1
temp= num & 1
print(temp == 1)
print("^^^^^^^^^^^^^^End of Worksheet 1 Solutions^^^^^^^^^^^^^^")