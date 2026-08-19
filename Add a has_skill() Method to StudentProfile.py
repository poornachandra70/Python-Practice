class StudentProfile:
    def __init__(self, student_id, name, course, score, skills, is_placed):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.score = score
        self.skills = skills
        self.is_placed = is_placed

    def has_skill(self, skill_name):
        # Search for skill_name case-insensitively and return True or False
        for skill in self.skills:
            if skill.strip().lower() == skill_name.strip().lower():
                return True
        return False

student_id = int(input())
name = input().strip()
course = input().strip()
score = float(input())
skills_input = input().strip()
placement_input = input().strip()
skill_to_find = input().strip()

skills = [
    skill.strip()
    for skill in skills_input.split(",")
    if skill.strip()
]

# Create exactly one StudentProfile object
student = StudentProfile(student_id, name, course, score, skills, placement_input)

# Call has_skill() and print the result based on the boolean return value
if student.has_skill(skill_to_find):
    print("Skill Found")
else:
    print("Skill Not Found")