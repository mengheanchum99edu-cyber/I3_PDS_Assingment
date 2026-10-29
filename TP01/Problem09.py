
# Problem 9: Electricity Bill with Progressive Tiers

# (a) Calculate the electricity bill
def electricity_bill(kwh):
    if kwh < 0:
        return None

    # Calculate consumption in each tier
    tier1 = min(kwh, 50)
    tier2 = min(max(kwh - 50, 0), 150)
    tier3 = max(kwh - 200, 0)

    # Calculate electricity cost
    cost = tier1 * 480 + tier2 * 610 + tier3 * 730

    # Add service fee
    cost += 2000

    # Add 10% VAT
    cost *= 1.10

    return round(cost)


# (b) Print the electricity bill table
print("Electricity Bill Table")
for kwh in (0, 35, 50, 120, 200, 350):
    bill = electricity_bill(kwh)
    usd = bill / 4100

    print(f"{kwh} kWh -> {bill:>9,} riel  (≈ {usd:>6.2f} USD)")


# (c) Ask the user for monthly consumption
kwh = float(input("\nEnter your monthly consumption (kWh): "))

bill = electricity_bill(kwh)

if bill is None:
    print("Invalid consumption. Please enter a non-negative number.")
else:
    usd = bill / 4100
    print(f"Your electricity bill: {bill:,} riel")
    print(f"Approximately: {usd:.2f} USD")
