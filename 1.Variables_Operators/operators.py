#Learning Arithmatic Operators
# a=2
# print(~a)
# print(a&1)
# print(a|2)
# print(a^3)
# a+=5
# print(a)

a=6745
d1=a//1000 #d1= 1
print(d1)

a=a-(1000*d1)  #a=234
d2=a//100 #d2 =2
print(d2)

a=a-(100*d2) # a=34
d3=a//10 #d3=3
print(d3)

a=a-(10*d3) # a=4
d4=a
print(d4)
print(d4,d3,d2,d1)
print(d4*1000 + d3*100 + d2*10 + d1)

# using 'is' identity operator
a="hello"
b="hello"
print(a is b) #True

num1 = 5
num2 = 5
print(num1 is num2) #True

a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a is b) #False
print(a is c) #True


