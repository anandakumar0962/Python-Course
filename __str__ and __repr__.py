class student:
    def __init__(self, stu_name, reg_no, dept):
        self.stu_name = stu_name
        self.reg_no = reg_no
        self.dept = dept
    
      # The __str__ or str() function returns a user-friendly description of an object.
    def __str__(self):
        return f' {self.stu_name} with register number {self.reg_no} from {self.dept} department'
           # The __repr__ or  repr() method returns a developer-friendly string representation of an object.
    def __repr__(self):
        return f' {self.stu_name}, {self.reg_no}, {self.dept}'
        
print(student('Anand', 'SP20ECU001', 'ECE'))