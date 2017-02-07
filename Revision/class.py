class s(str):
    __a=5
    def __init__(self,salary):
        self.salary=salary

emp=s(1000)
print(emp.salary)
emp.capitalize()
s.