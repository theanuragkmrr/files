class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printdata(self):
        return f"name is {self.name},age is {self.age}"

Anurag=Employee("Mannu",22)
Himanshu=Employee("Golu",23)
# Anurag.name="Mannu"
# Anurag.age=22
# Himanshu.name="Golu"
# Himanshu.age=23
# print(Himanshu.printdata())
print(Himanshu.age)

# class Employee:
#     def __init__(self,name,Empl_no,Role):
#         self.name = name
#         self.Empl = Empl_no
#         self.Role = Role
#     def print_det(self):
#         return f"Name is {self.name}.Employee number is {self.Empl}.Role is {self.Role}"
# Anurag=Employee("Anurag",2250282,"Graduate trainee")
#
# Himanshu=Employee("Himanshu",215566,"ASMT")
# Anurag.name="Anurag"
# Anurag.Empl=2250282
# Anurag.Role="Garaduate Trainee"