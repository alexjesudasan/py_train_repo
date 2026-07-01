# 1)Write a program for Electricity Bill Calculator that takes units consumed as input and calculates the bill
# First 100 units → ₹5/unit
# Next 100 units → ₹8/unit
# Above 200 units → ₹10/unit
units=int(input("enter units :"))
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 8
else:
    bill = (100 * 5) + (100 * 8) + (units - 200) * 10
print(f"EB bill amount to be paid is : {bill}")


# 2)Check if a given number is a palindrome (same forward and backward).
# Example: 121 → Palindrome, 123 → Not Palindrome.
#
# 3)Take an integer and find the largest digit using a while loop.
# Example: num = 94721 → Largest digit = 9.
#
# 4)Write a program that:
# If n is even → divide by 2
# If n is odd → multiply by 3 and add 1
# Repeat until n = 1.
# Example: 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1.
#
# 5)Take an integer and find the largest digit using a while loop.
# Example: num = 94721 → Largest digit = 9.