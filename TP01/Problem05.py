# Letter Grade
def letter_grade(score):
    if (score < 0 ) or (score > 100 ):
        grade = "Invalid"
    elif score >= 97:
        grade = "A+"
    elif score >= 90 :
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    return grade

# A. Test the function with the list
for score in [99, 90 ,85.5, 72, 60, 59.9, -5, 101]:
    print(f"{score} -> {letter_grade(score)}")

# B. Why must the test for A+ come before the test for A? What happens if you swap them?

# We must test for A+ before A because Python checks the conditions from top to bottom and executes the first condition that is True.
#If we swap the conditions, A+ will never be assigned, because every score greater than or equal to 97 also satisfies score >= 90.
