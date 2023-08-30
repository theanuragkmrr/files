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

    class player:
        games = 4

        def __init__(self, name, game):
            self.name = name
            self.game = game


class player:
    games = 4

    def __init__(self, name, game):
        self.name = name
        self.game = game
    def printdata(self):
        return f"name is {self.name},Game is {self.game} "
class coolprog(Employee,player):
    lang="C"
    def printlang(self):
        print(self.lang)


Anurag=Employee("Mannu",222,"instructor")
Himanshu=Employee("Golu",333,"destructor")
Keshav=coolprog("Keshav",566,"coolprogrammer")
det=Keshav.printdata()
Keshav.printlang()
print(det)