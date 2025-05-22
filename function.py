# def sumNumber(n1, n2):
#     sum = n1 + n2
#     return  sum
#
#
# while True:
#     n1 = int(input("Enter n1 :"))
#     n2 = int(input("Enter n2 : "))
#     sum = sumNumber(n1, n2)
#     print(sum)


# def myfunc(n1):
#     n1 = 10
#     print(f"Inside func n1 = {n1}")
#
# x = 20
# myfunc(x)
# print(x)


# def myfunc(n1 = 22):
#     print(f"Inside func n1 = {n1}")

# n1 = 11
# myfunc(n1)
# myfunc()


# def myfunc(n1,n3, n2 = 22):     #--------Default arguments are set at the end.
#     total = n1 + n2 + n3
#     return total
#
# n1 = 11
# n2 = 22
# n3 = 33
# myfunc(n1, n2, n3)


# def numbers(numbers):
#     numbers[0] = 22
#     for i in numbers:
#         print(i)
#
# n = [2,3,4,5,6,6]
# numbers(n)
#
# print(n)


# def numbers(numbers):
#     total = sum(numbers)
#     return total


# n = [1, 2, 3, 4, 5, 5, 6]
# total = numbers(n)

# print(total)
# print(n)


n = [1, 2, 3, 4, 5, 5, 6]
n2 = n
print(n)
print(n2)





# import turtle
#
#
# def draw_square(side_length):
#     for i in range(4):
#         turtle.forward(side_length)
#         turtle.left(90)
#
#
# counter = 0
# while counter < 90:
#     draw_square(100)
#     turtle.right(4)
#     counter += 1
# turtle.exitonclick()
