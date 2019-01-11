class Employee:
  def __init__(self,name,id,designation):
    self.name=name
    self.id=id
    self.designation=designation

  def print_values(self):
    print(self.name + "\n" + self.id + "\n" + self.designation)

name=input("Enter the name")
id=input("Enter the ID")
designation=input("enter the designation")
emp=Employee(name,id,designation)
emp.id="1000"
print(emp.id)
emp.print_values()


