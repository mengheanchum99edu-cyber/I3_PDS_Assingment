# Flexible Functions: *args, **kwargs and lambda


# (a) Flexible function using *args
def describe(*numbers, decimals=2, label="Data"):
    if not numbers:
        print(f"{label}: no values")
        return None

    count = len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    mean = sum(numbers) / count

    print(
        f"{label}: n={count} min={minimum} "
        f"max={maximum} mean={mean:.{decimals}f}"
    )

    return count, minimum, maximum, round(mean, decimals)


# (b) Flexible function using **kwargs
def make_tag(text, **style):
    attributes = ""

    for key, value in style.items():
        attributes += f' {key}="{value}"'

    return f"<span{attributes}>{text}</span>"


# (c) Lambda functions
square = lambda x: x ** 2
is_adult = lambda age: age >= 18


# Test the functions
describe(12, 7, 30, 4)
describe(3.14159, 2.71828, decimals=3, label="Constants")
describe()

print(make_tag("Hello", color="red", size=14))
print(square(9), is_adult(17), is_adult(21))
