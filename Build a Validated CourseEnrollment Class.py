class CourseEnrollment:
    def __init__(self, student_name, course_name):
        self.student_name = student_name
        self.course_name = course_name
        self.__status = "Enrolled"

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_status):
        valid_statuses = ["Enrolled", "Completed", "Dropped"]
        if new_status in valid_statuses:
            self.__status = new_status


student_name = input().strip()
course_name = input().strip()
new_status = input().strip()

enrollment = CourseEnrollment(student_name, course_name)
enrollment.status = new_status

print(f"Student: {enrollment.student_name}")
print(f"Course: {enrollment.course_name}")
print(f"Status: {enrollment.status}")