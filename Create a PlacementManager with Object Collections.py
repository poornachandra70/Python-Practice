class StudentProfile:
    def __init__(
        self,
        student_id,
        name,
        course,
        score,
        skills,
        is_placed
    ):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.score = score
        self.skills = list(skills)
        self.is_placed = is_placed


class JobDescription:
    def __init__(
        self,
        job_id,
        company,
        role,
        location,
        minimum_score,
        required_skills,
        is_active
    ):
        self.job_id = job_id
        self.company = company
        self.role = role
        self.location = location
        self.minimum_score = minimum_score
        self.required_skills = list(required_skills)
        self.is_active = is_active


class PlacementManager:
    def __init__(self):
        self.student_profiles = []
        self.job_descriptions = []


student_id = int(input())
name = input().strip()
course = input().strip()
score = float(input())
skills = [s.strip() for s in input().split(",")]
is_placed = input().strip()

job_id = int(input())
company = input().strip()
role = input().strip()
location = input().strip()
minimum_score = float(input())
required_skills = [s.strip() for s in input().split(",")]
is_active = input().strip()

student = StudentProfile(
    student_id,
    name,
    course,
    score,
    skills,
    is_placed
)

job = JobDescription(
    job_id,
    company,
    role,
    location,
    minimum_score,
    required_skills,
    is_active
)

# Create exactly one PlacementManager object
manager = PlacementManager()

# Store the complete student and job objects
manager.student_profiles.append(student)
manager.job_descriptions.append(job)

# Print the collection sizes and stored-record summaries
print(f"Student Profiles: {len(manager.student_profiles)}")
print(f"Job Descriptions: {len(manager.job_descriptions)}")

s_obj = manager.student_profiles[0]
j_obj = manager.job_descriptions[0]
print(f"Stored Student: {s_obj.student_id} - {s_obj.name}")
print(f"Stored Job: {j_obj.job_id} - {j_obj.role}")