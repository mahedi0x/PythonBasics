import time

print("Now i will complete the loop ")

# my name is mahedi hasan

# Python-এ লুপ হলো এমন একটি পদ্ধতি, যার মাধ্যমে আমরা একটি নির্দিষ্ট কাজ বারবার করাতে পারি, যতক্ষণ না কোন শর্ত পূরণ হয়।
# এতে কোড ছোট হয়, কাজ দ্রুত হয়।

# Python-এ লুপ দুই ধরনের
# 1. for loop
# 2. while loop

# -------------for loop------------

# for i in range(5):
#     print(i)

"""
sum = 0
for i in range(50):
    sum = sum + i
print(sum)
"""

# range(10)
# print(list(range(10)))


# ---------------------while loop-----------

# i = 0
# while i <= 5:
#     print(i)
#     i += 1

#
# while True:
#     num = int(input())
#     if num == 0:
#         break
#     print(f"Num is", num)


"""
while True:
    num = int(input())
    if num < 0:
        print("Please give me Positive Number")
        continue
    elif num == 0:
        print("We found zero , so program will be stop ")
        break
    else:
        print(num)
"""

"""
num = int(input("Enter a Number for Multiplication Table: "))
n = 1
while n <= 10:
    time.sleep(.5)
    print(num, "X", n, "=", num * n)
    n += 1

"""

terminate = False
while not terminate:
    num1 = int(input("Enter num1 : "))
    num2 = int(input("Enter num2 : "))
    while True:
        operation = input("add/sub or quit : ")
        if operation == "quit":
            terminate = True
            break

        elif operation == "add":
            print("addition is = ", num1 + num2)
            break
        elif operation == "sub":
            print("Sub is = ", num1 - num2)
            break
        elif operation not in ["add", "sub"]:
            print("Unknown Operation !!!")
            continue

"""
for sec in range(1,10):
    print(f"{sec} sec gone")
    time.sleep(1)
print("time is over")

"""

"""
import turtle

turtle.color("black")
turtle.speed(6)
counter = 0
while counter < 36:
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.right(10)
    counter += 1
turtle.exitonclick()
"""
