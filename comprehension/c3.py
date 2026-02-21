# remove duplicate elements from a list using a set and print only values greater than 5.

list1 = [1, 2, 2, 1, 3, 3, 5, 4, 3, 4, 5, 6, 7, 7, 6, 8, 9, 5, 9, 8]

# remove duplicates using set
set1 = set(list1)

# print values greater than 5
res = [x for x in set1 if x > 5]

print(res)