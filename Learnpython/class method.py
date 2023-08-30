class Employee:
    no_of_leaves=8

    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printdata(self):
        return f"name is {self.name},age is {self.age}"


    @classmethod
    def change_leaves(cls,newl):
        cls.no_of_leaves=newl

Anurag=Employee("Mannu",22)
Himanshu=Employee("Golu",23)
Anurag.change_leaves(34)
print(Employee.no_of_leaves)
