# Part A

print(int ("7") + 3.5)
print(str(10)*3)
print(bool(""), bool(" "))
print(int(3.99))
print(float("1e3"))
print(int(True) + float("2.5"))
print(round(2.5), round(3.5))
print(type(10 / 2))

# Part B

def safe_int(text):
    try:
        return int(float(text.strip()))
    except:
        None
# repr is useful for debuging becase ' -8 'epr() helps you see spaces and quotation marks clearly, which is useful for checking data.
for sample in ["42", " -8", "3.9", "abc", ""]:
    print(repr(sample), " -> ", safe_int(sample))

# Part C


def sum(number1, number2):
    return number1+number2

try:
    number1 = int(input("Please enter the number 1 : "))
    number2 = int(input("Please enter the number 2 : "))
    print(f"The sum of {number1} and {number2} is {sum(number1,number2)}")
except  ValueError:
    print("PLEASE ENTER ONLY NUMBER !!!")
    

