# create a set of numbers that are divisible by both 3 and 5 between 1 and 50.

st1 = {x for x in range(1, 51) if x % 3 == 0 and x % 5 == 0}

print(st1)