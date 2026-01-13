import sys

# Make sure 5 marks are provided
if len(sys.argv) != 6:
    print("Usage: python student_grade.py mark1 mark2 mark3 mark4 mark5")
    sys.exit()

# Convert each argument individually
m1 = float(sys.argv[1])
m2 = float(sys.argv[2])
m3 = float(sys.argv[3])
m4 = float(sys.argv[4])
m5 = float(sys.argv[5])

# Calculate average
avg = (m1 + m2 + m3 + m4 + m5) / 5

# Determine grade
if avg >= 90:
    grade = 'A'
elif avg >= 75:
    grade = 'B'
elif avg >= 60:
    grade = 'C'
elif avg >= 50:
    grade = 'D'
else:
    grade = 'Fail'

print(f"Average: {avg:.2f}")
print(f"Grade: {grade}")
