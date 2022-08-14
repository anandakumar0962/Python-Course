
# Inheritance means the reuse of codes. Here Class Inheritance is done.
# Creating a python program using class inheritance to know
      # Basic salary for a fresher,
      # Eligibility of promotion,
      # And salary hike of an employee in a company.


class Employee:   # class name

    salary = 10000   # class variable
    
    def __init__(self, name, emp_id, dept, yr_of_exp):  # __init__ is a default method in class
        self.name = name
        self.emp_id = emp_id
        self.dept = dept
        self.yr_of_exp = yr_of_exp

        
    @classmethod    # class method calls classname as the first argument.
    def emp_data(cls, data):   # cls means the class name  
        name, emp_id, dept, yr_of_exp = data.split(",")  # split() function is used to split the string 
        return cls(name, emp_id, dept, yr_of_exp)

    
    @classmethod  # class method calls classname as the first argument.
    def basic_salary(cls, dept):    # The basic salary method is used to define the basic salary of an employee based on the department
        if dept == 'electrical':
            salary = 12000
            return salary
        if dept == 'production':
            salary = 11500
            return salary
        if dept == 'maintanance':
            salary = 11000
            return salary

        
    @staticmethod    # static method is a method which don't call both object and classname
    def promotion(exp):
        if exp >= 2:
            print("Eligible")
        else:
            print("Not Eligible")

# Inheritance of class            
class Salary_hike(Employee):  # In which the class Salary_hike inherits the arguments of class Employee 
    
    def __init__(self, name, emp_id, dept, yr_of_exp, current_salary):
        super().__init__(name, emp_id, dept, yr_of_exp)  # super() function is used to overcome the rewrite of the code 
        self.current_salary = current_salary

        
    @classmethod
    def increment_salary(cls, dept, yr_of_exp):
        if dept == 'electrical':
            salary = yr_of_exp*1500 + 12000
            return salary
        if dept == 'production':
            salary = yr_of_exp*1200 + 11500
            return salary
        if dept == 'maintanance':
            salary = yr_of_exp*1000 + 11000
            return salary


emp1 = Employee('Anand', 'emp_E01', 'electrical', 3)
emp2 = Employee('Hari Haran', 'emp_P12', 'production', 2)
data = 'Vignesh,emp_M24,mechanical,1'
emp3 = Employee.emp_data(data)


print(emp3.name)
print(emp1.dept)
print(Employee.basic_salary('production'))
print(emp1.promotion(3))
print(Salary_hike.increment_salary('electrical', 2))
