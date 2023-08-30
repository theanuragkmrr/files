class Dad:
    dances=1
class Son(Dad):
    dances=2
    def dance(self):
        return f"I am dancer{self.dances}"
class Grandson(Son):
    dances = 4

    def dance(self):
        return f"I am a disco and hip hop dancer {self.dances}"

Darry=Dad()
larry=Son()
Harry=Grandson()
print(Darry.dances)