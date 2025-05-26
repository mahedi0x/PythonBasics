
# ------------------------LIST--------------------

a = []
names = ["Mahedi", "Hasan", "Bulbul"]
numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[-1])

mixed = [10, "Mahedi", 30.23, True]



# ------------LIST METHODS --------------------
# 1.append()   --------    7.index()
# 2.copy()     --------    8.pop()
# 3.clear()    ---------   9.remove()
# 4.count()    ---------   10.reverse()
# 5.extend()   ---------   11.sort()
# 6.insert()



# 1. append() ----- add element to the list
a = [1, 2, 3, 4]
a.append(5)
print(a)



 # 2. copy() ----- create a copy of list
a = [1, 2, 3, 4]
b = a.copy()
print(a)
# print(b) --- we get same value



# 3. clear() ----- clear all elements from the list
a = [1, 2, 3, 4]
a.clear()
# print(a) -----we get an empty list



# 4. count() -- count the occurrences of a specific element in the list
a = [1, 2, 3, 4, 2, 5, 6, 2, 6]
print(a.count(2)) --- 4



# 5. extend(). ---- extend() the list by adding elements from another list
a = [1, 2, 3,]
a.extend([5,6])
# print(a) --- now we get [1, 2, 3, 4, 5, 6]



# 6. index() --- find the index of a specific element in the list
a = [1, 2, 3, 4, 2]
# print(a.index(2)) ---- we get 1. element 2 have in index 1



# 7. insert() ---insert an element of a specific positon in the list
a = [1, 2, 4, 5]
a.insert(0,3)
print(a)



# 8. pop() -- remove the last element of the list
a = [1, 2, 3, 4]
a.pop()
print(a)



# 9. remove() -- remove the first occurrence of a specified element from the list
a = [1, 2, 3, 4]
a.remove(4)
print(a)



# 10. reverse() --- reverse the order of the elements of the list
a = [1, 2, 3, 4]
a.reverse()
print(a)



# 11. sort() -- sort the elements of the list in ascending order
a = [3, 1, 4, 2]
a.sort()
print(a)



# --------------------List ( Question & Solve )----------------
# remove duplicate elements

n = int(input())
unique = []
for i in range(n):
    num = int(input())
    if num not in unique:
        unique.append(num)

print(unique)


















