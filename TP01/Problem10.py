
# Problem 10: Prime Numbers and Goldbach's Conjecture

# (a) Check whether a number is prime
def is_prime(n):
    if n < 2:
        return False

    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1

    return True


# (b) Print all primes below 50
print("Primes below 50:", end=" ")

for n in range(2, 50):
    if is_prime(n):
        print(n, end=" ")

print()

# Count primes below 100
count = 0

for n in range(2, 100):
    if is_prime(n):
        count += 1

print(f"Number of primes below 100: {count}")


# (c) Find the first pair of primes whose sum is n
def goldbach(n):
    for p in range(2, n):
        if is_prime(p):
            q = n - p

            if is_prime(q):
                return p, q

    return None


# Print Goldbach pairs for even numbers from 4 to 30
for n in range(4, 31, 2):
    pair = goldbach(n)
    print(f"{n} = {pair[0]} + {pair[1]}")


# (d) Check Goldbach's conjecture up to 10,000
goldbach_holds = True

for n in range(4, 10001, 2):
    if goldbach(n) is None:
        goldbach_holds = False
        break

print(
    "Goldbach holds for every even number from 4 to 10000:",
    goldbach_holds
)
