class A:
    classvar1="I am aclass variable in class A"
    def __init__(self):
        self.var1="I am inside class A'constructor "
        self.classvar1="I am a clas A instance"
        self.special="Special"
class B(A):
    classvar1 = "I am a class B Vareiable"
    def __init__(self):
        super().__init__()
        self.var1="I am inside class B'constructor "
        self.classvar1="I am a clas B instance"
        # super().__init__() #for overring class A on B

a=A()
b=B()
# print(b.classvar1) #always find instance vaariable first
# print(b.var1)# always fing own class instance first
print(b.special,b.var1,b.classvar1)