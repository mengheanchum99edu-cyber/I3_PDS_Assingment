
# Problem 2: Time Converter

total_seconds = 9875

# (a) Convert seconds into hours, minutes, and seconds
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"{total_seconds} seconds = {hours} h {minutes} min {seconds} s")

# (b) Rebuild the total to check the answer
check = (hours * 3600 + minutes * 60 + seconds) == total_seconds
print(f"Check: {check}")

# (c) Test with other values
for total_seconds in (3600, 59, 86399):
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    print(f"{total_seconds} seconds = {hours} h {minutes} min {seconds} s")
