class StudentProfile:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course


class JobDescription:
    def __init__(self, job_id, company, role):
        self.job_id = job_id
        self.company = company
        self.role = role


class PlacementManager:
    def __init__(self):
        self.student_profiles = []
        self.job_descriptions = []

    def add_student_profile(self, student_profile):
        self.student_profiles.append(student_profile)

    def add_job_description(self, job_description):
        self.job_descriptions.append(job_description)

    def find_student_by_id(self, student_id):
        for student in self.student_profiles:
            if student.student_id == student_id:
                return student
        return None

    def find_job_by_id(self, job_id):
        for job in self.job_descriptions:
            if job.job_id == job_id:
                return job
        return None


manager = PlacementManager()

student_count = int(input())
for _ in range(student_count):
    student_id = int(input())
    name = input().strip()
    course = input().strip()
    student = StudentProfile(student_id, name, course)
    manager.add_student_profile(student)

job_count = int(input())
for _ in range(job_count):
    job_id = int(input())
    company = input().strip()
    role = input().strip()
    job = JobDescription(job_id, company, role)
    manager.add_job_description(job)

student_id_to_find = int(input())
job_id_to_find = int(input())

# Search for the student and job
found_student = manager.find_student_by_id(student_id_to_find)
found_job = manager.find_job_by_id(job_id_to_find)

# Display the search results
if found_student:
    print(f"Student Found: {found_student.student_id} - {found_student.name} - {found_student.course}")
else:
    print("Student Not Found")

if found_job:
    print(f"Job Found: {found_job.job_id} - {found_job.company} - {found_job.role}")
else:
    print("Job Not Found")