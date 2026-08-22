class JobDescription:
    def __init__(self, role, required_skills):
        self.role = role
        self.__required_skills = list(required_skills)

    @property
    def required_skills(self):
        return self.__required_skills

    def add_required_skill(self, skill):
        if skill not in self.__required_skills:
            self.__required_skills.append(skill)


role = input().strip()
skills = [skill.strip() for skill in input().split(",")]
new_skill = input().strip()

job = JobDescription(role, skills)
job.add_required_skill(new_skill)

print(f"Job Role: {job.role}")
print(f"Required Skills: {', '.join(job.required_skills)}")