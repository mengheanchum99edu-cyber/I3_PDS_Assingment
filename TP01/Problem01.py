#Problem01: Student Profile Card

name = "CHUM Menghean"
age = 21
major = "Data Science"
gpa = 3.0
is_scholar = True 

# (a) Print the profile card
print("=================================")
print("Name\t:", name)
print("Age\t:", age)
print("Major\t:", major)
print(f"GPA\t:{gpa:.2f}")
print("Scholar\t:", is_scholar)
print("=================================")

# (b) Print each value and its type
print(name ,"->", type(name))
print(age ,"->", type(age))
print(major ,"->", type(major))
print(gpa ,"->", type(gpa))
print(is_scholar ,"->", type(is_scholar))

# (c) Re-assign age as a string
age = "20"
print(age ,"->", type(age))