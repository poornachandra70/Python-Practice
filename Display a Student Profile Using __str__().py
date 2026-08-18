class StudentProfile:
    def __init__(self, student_id, name, course, score, skills, is_placed):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.score = score
        self.skills = skills
        self.is_placed = is_placed

    def __str__(self):
        placement_status = "Placed" if self.is_placed else "Not Placed"
        skills_str = ", ".join(self.skills)
        return (
            f"Student ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Course: {self.course}\n"
            f"Score: {self.score:.1f}\n"
            f"Skills: {skills_str}\n"
            f"Placement Status: {placement_status}"
        )


# Read inputs
student_id = int(input())
name = input()
course = input()
score = float(input())
skills_input = input()
placement_input = input()

# Process skills
skills = [skill.strip() for skill in skills_input.split(",")]

# Convert placement status
is_placed = placement_input.strip().lower() == "yes"

# Create one StudentProfile object
student = StudentProfile(student_id, name, course, score, skills, is_placed)

# Display the object using print(student)
print(student)