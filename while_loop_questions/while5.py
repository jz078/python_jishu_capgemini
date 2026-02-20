# given a number, check whether it is a palindrome or not.

def reverse_number(num):
    rev = 0

    while(num > 0):
        digit = num%10
        rev *= 10
        rev += digit
        num //= 10

    return rev
        


num = int(input("Enter a number : "))

rev = reverse_number(num)

if(rev == num):
    print(num, " is palindrome")
else:
    print("not palindrome")