class Employee:
    def __init__(self, id: int, firstName: str, lastName: str, salary: int) -> None:
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary
        
    def get_id(self):
        return self.id
    
    def get_first_name(self):
        return self.firstName
    
    def get_last_name(self):
        return self.lastName
    
    def get_name(self):
        return f"{self.firstName} {self.lastName}"
    
    def get_salary(self):
        return self.salary
    
    def set_salary(self, salary):
        self.salary = salary

    def get_annual_salary(self):
        return self.salary * 12
    
    def raise_salary(self, percent):
        self.salary += self.salary * percent // 100
        return self.salary
    
    def __str__(self) -> str:
        return f"Employee[id= {self.id}], Name= {self.firstName} {self.lastName}, Salary= {self.salary}"
    
employee1 = Employee(1, "Dilshodbek", "Xolmirzayev", 5000)

print(employee1)

print(employee1.get_name())

employee1.set_salary(6000)
print(employee1.get_salary())

print(employee1.get_annual_salary())

employee1.raise_salary(10)
print(employee1.get_salary())

print(employee1)
