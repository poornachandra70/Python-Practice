class StudentProfile:
    def __init__(self, name):
        self.__name = name.strip()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        cleaned_name = new_name.strip()
        if cleaned_name != "":
            self.__name = cleaned_name


initial_name = input()
new_name = input()

student = StudentProfile(initial_name)
student.name = new_name

print(f"Student Name: {student.name}")