class Laptop:
    def __init__(self,price,model,color):
        self.price=price
        self.model=model
        self.color=color
        self.laptop_name=model +" "+ color

lapy=Laptop(134000,"25xcf","silver")
print(lapy.laptop_name)