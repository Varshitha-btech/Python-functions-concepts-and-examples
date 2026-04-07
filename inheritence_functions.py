class Employee:
    company_name="HCL"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display_details(self):
        print("Name is:",self.name)
        print("Salary id:",self.salary)
        print("Company_name:",Employee.company_name)
emp1=Employee("varsha",100000)
emp2=Employee("geeta",1000000)
emp1.display_details()
emp2.display_details()
print("change the company name")
Employee.company_name="TCS"
emp1.display_details()
emp2.display_details()
        