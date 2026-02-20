# count how many times a specific digit apperas in a number.

org_num = int(input("Enter a number: "))
digit = int(input("Enter a specific digit to count in the number: "))

num = org_num
count = 0

while num>0:
    curr_digit = num%10
    if(curr_digit == digit):
        count+=1
    num //= 10

print(digit, " appears ", count, " times in ", org_num)