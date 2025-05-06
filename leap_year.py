year = int(input("Enter a Year : "))

if year % 4 == 0 and year % 100 != 0:
    print("Yes")
elif year % 100 == 0 and year % 400:
    print("Yes")
else:
    print("Not Leap Year.")
