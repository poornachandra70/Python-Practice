class StudentProfile:
    def __init__(self, score):
        self.__score = 0
        # Assign the score using the property
        self.score = score

    @property
    def score(self):
        # Return the stored score
        return self.__score

    @score.setter
    def score(self, new_score):
        # Validate and store the score
        if 0 <= new_score <= 100:
            self.__score = new_score


score = int(input())
student = StudentProfile(score)

print(f"Score: {student.score}")