# count how many even and odd digits are present in a given number.

def even_odd_count(num):
    even = 0
    odd = 0

    while num>0 :
        digit = num % 10
        if(digit % 2 == 0):
            even += 1
        else:
            odd += 1
        
        num //= 10
    
    return even, odd

num = int(input("Enter a number: "))
tuple = even_odd_count(num)

print("even digits:", tuple[0])
print("odd digits: ", tuple[1])