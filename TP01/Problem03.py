
# Problem 3: Temperature Converter

def celsius_to_fahrenheit(celsius, round_to=1):
    fahrenheit = (celsius * 9 / 5) + 32
    return round(fahrenheit, round_to)


def fahrenheit_to_celsius(fahrenheit, round_to=1):
    celsius = (fahrenheit - 32) * 5 / 9
    return round(celsius, round_to)


# (a) Print the conversion table
print("  °C  |   °F")
print("------+-------")

for celsius in range(0, 101, 20):
    print(f"{celsius:5} | {celsius_to_fahrenheit(celsius):5.1f}")


# (b) Convert 98.6 °F to Celsius
print(
    f"\nNormal body temperature in Celsius: "
    f"{fahrenheit_to_celsius(98.6)} °C"
)


# (c) Convert 37 °C to Fahrenheit and back to Celsius
fahrenheit = celsius_to_fahrenheit(37)
print(f"37 °C in Fahrenheit: {fahrenheit} °F")

celsius_again = fahrenheit_to_celsius(fahrenheit)
print(f"Converted back to Celsius: {celsius_again} °C")

# Yes, we get 37.0 °C again.


# (d) Call a function with round_to=3
print(f"\n37 °C in Fahrenheit (3 decimal places): "
      f"{celsius_to_fahrenheit(37, round_to=3)}")

# A default argument is useful because we do not need to specify round_to every time. We can change it when needed.
