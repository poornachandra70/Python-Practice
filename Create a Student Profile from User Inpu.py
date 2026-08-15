class StudentProfile:
    def __init__(self, student_id, name, course, score, skills, is_placed):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.score = score
        self.skills = skills
        self.is_placed = is_placed


# Read input
student_id = int(input())
name = input().strip()
course = input().strip()
score = float(input())
skills_input = input().strip()
placement_input = input().strip()


# Convert skills_input into a list of skill names
skills = [skill.strip() for skill in skills_input.split(",")]


# Convert placement_input into a Boolean value
is_placed = placement_input.lower() == "yes"


# Create one StudentProfile object
student = StudentProfile(
    student_id,
    name,
    course,
    score,
    skills,
    is_placed
)


# Print the stored student details
print("Student ID:", student.student_id)
print("Name:", student.name)
print("Course:", student.course)
print("Score:", student.score)
print("Skills:", ", ".join(student.skills))

if student.is_placed:
    print("Placement Status: Placed")
else:
    print("Placement Status: Not Placed")