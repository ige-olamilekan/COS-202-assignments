print("=" * 50)
print("     PERSONAL POCKET CGPA CALCULATOR (PPC)")
print("=" * 50)

total_units = 0
total_points = 0

num_courses = int(input("How many courses do you want to enter? "))

print("\nFor each course, enter the course code, credit unit, and score.\n")

for i in range(num_courses):
    print(f"--- Course {i + 1} ---")
    code = input("Course code: ")
    units = int(input("Credit unit: "))
    score = float(input("Score (0-100): "))

    # Selection control statements to assign grade and point
    if score >= 70:
        grade = 'A'
        point = 5
    elif score >= 60:
        grade = 'B'
        point = 4
    elif score >= 50:
        grade = 'C'
        point = 3
    elif score >= 45:
        grade = 'D'
        point = 2
    elif score >= 40:
        grade = 'E'
        point = 1
    else:
        grade = 'F'
        point = 0

    print(f"-> {code}: Grade {grade}, Grade Point {point}\n")

    total_units += units
    total_points += (point * units)

gpa = total_points / total_units

print("=" * 50)
print(f"Total Units: {total_units}")
print(f"Total Grade Points: {total_points}")
print(f"YOUR GPA: {gpa:.2f}")

# Classification using selection control statements
if gpa >= 4.50:
    remark = "First Class"
elif gpa >= 3.50:
    remark = "Second Class Upper"
elif gpa >= 2.40:
    remark = "Second Class Lower"
elif gpa >= 1.50:
    remark = "Third Class"
elif gpa >= 1.00:
    remark = "Pass"
else:
    remark = "Fail"

print(f"Classification: {remark}")
print("=" * 50)''