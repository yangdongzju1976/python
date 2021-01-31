class Employee:
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount=1
    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)
    def displayEmployee(self):
        print("name:",self.name,"Salary",self.salary)
#创建类的对象
emp1=Employee("Manni",5000)
emp2=Employee("Sara",2000)
emp1.displayEmployee()
emp2.displayEmployee()
