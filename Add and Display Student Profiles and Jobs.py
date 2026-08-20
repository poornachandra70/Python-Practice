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

    def __str__(self):
        return f"{self.student_id} - {self.name} - {self.course}"


class JobDescription:
    def __init__(
        self,
        job_id,
        company,
        role,
        location="Remote",
        minimum_score=0.0,
        required_skills=None,
        is_active=True
    ):
        self.job_id = job_id
        self.company = company
        self.role = role
        self.location = location
        self.minimum_score = minimum_score
        self.required_skills = (
            []
            if required_skills is None
            else list(required_skills)
        )
        self.is_active = is_active

    def __str__(self):
        return f"{self.job_id} - {self.company} - {self.role}"


class PlacementManager:
    def __init__(self):
        # Creates student_profiles and job_descriptions as separate empty lists
        self.student_profiles = []
        self.job_descriptions = []

    def add_student_profile(self, student_profile):
        # Add the complete student object
        self.student_profiles.append(student_profile)

    def add_job_description(self, job_description):
        # Add the complete job object
        self.job_descriptions.append(job_description)

    def display_student_profiles(self):
        # Display the heading, records or empty message
        print("STUDENT PROFILES")
        if not self.student_profiles:
            print("No student profiles available")
        else:
            for student in self.student_profiles:
                print(student)

    def display_job_descriptions(self):
        # Display the heading, records or empty message
        print("JOB DESCRIPTIONS")
        if not self.job_descriptions:
            print("No job descriptions available")
        else:
            for job in self.job_descriptions:
                print(job)


# Creates exactly one PlacementManager object
manager = PlacementManager()

student_count = int(input())
for _ in range(student_count):
    student_id = int(input())
    name = input().strip()
    course = input().strip()
    score = float(input())
    skills_input = input().strip()
    placement_input = input().strip()

    skills = [
        skill.strip()
        for skill in skills_input.split(",")
        if skill.strip()
    ]
    is_placed = placement_input.lower() == "yes"

    student = StudentProfile(
        student_id,
        name,
        course,
        score,
        skills,
        is_placed
    )
    # Add the student through the manager method
    manager.add_student_profile(student)

job_count = int(input())
for _ in range(job_count):
    job_id = int(input())
    company = input().strip()
    role = input().strip()
    location = input().strip()
    minimum_score = float(input())
    required_skills_input = input().strip()
    job_status_input = input().strip()

    required_skills = [
        skill.strip()
        for skill in required_skills_input.split(",")
        if skill.strip()
    ]
    is_active = job_status_input.lower() == "yes"

    job = JobDescription(
        job_id,
        company,
        role,
        location,
        minimum_score,
        required_skills,
        is_active
    )
    # Add the job through the manager method
    manager.add_job_description(job)

# Calls both display methods after all records have been added
manager.display_student_profiles()
manager.display_job_descriptions()