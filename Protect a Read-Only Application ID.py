class CandidateApplication:
    def __init__(self, application_id, candidate_name):
        self.__application_id = application_id
        self.candidate_name = candidate_name

    @property
    def application_id(self):
        return self.__application_id


application_id = input().strip()
candidate_name = input().strip()

application = CandidateApplication(application_id, candidate_name)

print(f"Application ID: {application.application_id}")
print(f"Candidate Name: {application.candidate_name}")