class StudentProfile:
    pass

# Read the student's name
name = input().strip()

# Create a StudentProfile object
student = StudentProfile()

# Store the name in the object
student.name = name

# Print the stored name
print(f"Student Name: {student.name}")