marks = int(input())
# Check whether the marks are valid
if marks < 0 or marks > 100:
    print("Invalid Marks")
elif marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: F")

