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
        # Store all instance attributes
        self.job_id = job_id
        self.company = company
        self.role = role
        self.location = location
        self.minimum_score = minimum_score
        
        if required_skills is None:
            self.required_skills = []
        else:
            self.required_skills = required_skills
            
        self.is_active = is_active

    def __str__(self):
        # Return the complete formatted job description
        skills_str = ", ".join(self.required_skills)
        status_str = "Active" if self.is_active else "Closed"
        return (f"Job ID: {self.job_id}\n"
                f"Company: {self.company}\n"
                f"Role: {self.role}\n"
                f"Location: {self.location}\n"
                f"Minimum Score: {self.minimum_score:.1f}\n"
                f"Required Skills: {skills_str}\n"
                f"Status: {status_str}")

# Read the details from the user
job_id = int(input())
company = input().strip()
role = input().strip()
location = input().strip()
minimum_score = float(input())
skills_input = input().strip()
status_input = input().strip()

# Convert the comma-separated skills input into a list of cleaned skill names
required_skills = [
    skill.strip() 
    for skill in skills_input.split(",") 
    if skill.strip()
]

# Convert the job-status input into a Boolean value
is_active = status_input.strip().lower() == "yes"

# Create exactly one JobDescription object
job = JobDescription(
    job_id=job_id,
    company=company,
    role=role,
    location=location,
    minimum_score=minimum_score,
    required_skills=required_skills,
    is_active=is_active
)

# Print the created object directly
print(job)