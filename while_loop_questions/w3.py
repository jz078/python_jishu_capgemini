# given a number, repeatedly sum its digits until a single digit is obtained.

def sum_of_digit(num):
    sum = 0
    while(num>0):
        digit = num%10
        sum += digit
        num //= 10

    return sum


num = int(input("Enter a number : "))

sum = 0

while len(str(num)) != 1 : 
    sum = sum_of_digit(num)
    num = sum

print(sum)