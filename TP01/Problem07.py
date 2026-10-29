# Digit Tools

# Function use to add each digit
def digit_sum(n):
    n = abs(n)
    sum = 0
    while n > 0 :
        last_digit = n %  10
        n //= 10
        sum +=  last_digit
    return sum

def reverse_number(n):
    n = abs(n)
    reversed_num = 0
    while n > 0 :
        last_digit = n % 10
        reversed_num = reversed_num * 10 + last_digit
        n //= 10

    return reversed_num

def is_palindrome(n):
    if n < 0:
        return False
    return n == reverse_number(n)

#Test the three functions with 2026, 12321 and 9875. 

for n in (2026, 12321, 9875):
    print(f"{n}: digit sum = {digit_sum(n)}, reversed = {reverse_number(n)}, palindrome = {is_palindrome(n)}")

# (b) Count how many palindromes there are from 10 to 999.

count_palindrome = 0
for n in range(10,1000):
    if is_palindrome(n) == True:
        count_palindrome += 1   
print(f"Palindromes from 10 to 999: {count_palindrome}")