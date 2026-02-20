# keep accepting numbers until the sum exceeds 100.

limit = 100

sum = 0

while(sum <= limit):
    num = int(input("Enter number to add to sum: "))
    sum += num
    print("sum:", sum)

print("sum exceeds 100")
print("sum is", sum)