class StudentProfile:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name


class JobDescription:
    def __init__(self, job_id, role):
        self.job_id = job_id
        self.role = role


class PlacementManager:
    def __init__(self):
        self.students = []
        self.jobs = []

    def add_student(self, student):
        self.students.append(student)

    def add_job(self, job):
        self.jobs.append(job)

    def search_student(self, student_id):
        for student in self.students:  # Make sure this is self.students (plural)
            if student.student_id == student_id:
                return student
        return None

    def search_job(self, job_id):
        for job in self.jobs:  # Make sure this is self.jobs (plural)
            if job.job_id == job_id:
                return job
        return None


# Driver Code / Main Execution
manager = PlacementManager()

# Input students
for _ in range(int(input())):
    student = StudentProfile(int(input()), input().strip())
    manager.add_student(student)

# Input jobs
for _ in range(int(input())):
    job = JobDescription(int(input()), input().strip())
    manager.add_job(job)

student_id = int(input())
job_id = int(input())

# Display collection sizes and search results
print(f"Students: {len(manager.students)}")
print(f"Jobs: {len(manager.jobs)}")

found_student = manager.search_student(student_id)
if found_student:
    print(f"Student: {found_student.student_id} - {found_student.name}")
else:
    print("Student Not Found")

found_job = manager.search_job(job_id)
if found_job:
    print(f"Job: {found_job.job_id} - {found_job.role}")
else:
    print("Job Not Found")