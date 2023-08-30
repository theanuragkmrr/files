class Employee:
    no_of_leaves=8

    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
    def printdata(self):
        return f"name is {self.name},salary is {self.salary} and role is {self.role}"


    @classmethod
    def change_leaves(cls,newl):
        cls.no_of_leaves=newl

    @classmethod
    def from_str(cls,str):
        # params=str.split("-")
        # return cls(params[0],params[1])
        return cls(*str.split("-")) #from args in one line

    @staticmethod
    def printgd(str):
        print ("This is good " +str)
class programmer(Employee):
    def __init__(self,name,salary,role,lang):
        self.name=name
        self.salary=salary
        self.role=role
        self.lang=lang
    def prog(self):
        return f"The programmer is {self.name},salary is {self.salary},role is {self.role} and languages are {self.lang}"

Anurag=Employee("Mannu",222,"instructor")
Himanshu=Employee("Golu",333,"destructor")
# harry=Employee.from_str("Harry-30")
# Anurag.change_leaves(34)
# print(Employee.no_of_leaves)
# Employee.printgd("harry")
# print(Anurag.role)
Keshav=programmer("Keshav",555,"Programmer",["python","cpp"])
Nishant=programmer("Nishant",666,"Programmer",["python"])
Manan=programmer("Manan",777,"Programmer",["python"])
Ajay=programmer("Ajay",888,"Programmer",["python"])
print (Nishant.prog())