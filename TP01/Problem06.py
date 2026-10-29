# Leap Years a d Days in Month

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(month, year):
    if month < 1 or month > 12:
        return None

    if month == 2:
        if is_leap(year):
            return 29
        return 28

    if month in (4, 6, 9, 11):
        return 30

    return 31


# (c) Check leap years
for year in (1900, 2000, 2024, 2026):
    if is_leap(year):
        print(year, "leap")
    else:
        print(year, "not leap")


# Check the number of days in different months
print(
    f"Feb 2024: {days_in_month(2, 2024)}"
    f" | Feb 2026: {days_in_month(2, 2026)}"
    f" | Apr: {days_in_month(4, 2024)}"
    f" | month 13: {days_in_month(13, 2024)}"
)


# (d) Count leap years from 2000 to 2100
count = 0

for year in range(2000, 2101):
    if is_leap(year):
        count += 1

print(f"Leap years from 2000 to 2100: {count}")
