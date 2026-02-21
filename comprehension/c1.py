# create a list of squares of even numbers only from a given list.

nums = [1, 2, 3, 4, 5, 6, 7, 8]

sq = [x*x for x in nums if x % 2 == 0]

print(sq)