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

    @classmethod
    def from_str(cls,str):
        # params=str.split("-")
        # return cls(params[0],params[1])
        return cls(*str.split("-")) #from args in one line

Anurag=Employee("Mannu",22)
Himanshu=Employee("Golu",23)
harry=Employee.from_str("Harry-30")
Anurag.change_leaves(34)
print(Employee.no_of_leaves)
print(harry.age)
skillf=Employee("Anuragaag",66)
print(skillf.name)