"""
num = int(input("Enter a number : "))

if num % 2 == 0:
    print("Number is Even.")
else:
    print("Number is Odd.")
"""

num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 > num2 and num1 > num3:
    print("Max number is = ", num1)
elif num2 > num1 and num2 > num3:
    print("Max number is = ", num2)
else:
    print("Max number is ", num3)
