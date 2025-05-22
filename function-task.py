# #------------ Find Average from list ----------
#
# def average_find(numbers):
#     length = len(numbers)
#     average = sum(numbers) / length
#     return average
#
#
# numbers = [2,4,5,6]
# average = average_find(numbers)
# print(average)




# -------------create Multiplication table--------------
def multiplication_table(n = 1):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")

n = int(input("Enter a Number for Multiplication Table: "))
multiplication_table(n)