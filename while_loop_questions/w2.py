# reverse a number using a while loop and check whether the reversed number is greater than the original

def reverse(num: int):
    return int(str(num)[::-1])

num = int(input("Enter a number : ")) 

rev = reverse(num)

if rev >= num:
    print("reverse is greater than original")