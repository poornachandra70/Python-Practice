class Employee:
    def __init__(self, employee_id, name, salary):
        self.__employee_id = employee_id
        self.name = name
        self.__salary = salary

    @property
    def employee_id(self):
        return self.__employee_id

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value >= 0:
            self.__salary = value


employee_id = input().strip()
name = input().strip()
salary = int(input())
new_salary = int(input())

employee = Employee(employee_id, name, salary)
employee.salary = new_salary

print(f"Employee ID: {employee.employee_id}")
print(f"Name: {employee.name}")
print(f"Salary: {employee.salary}")