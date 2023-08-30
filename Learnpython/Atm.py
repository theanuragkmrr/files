class Atm():
    def __init__(self):
        self.Balance=0
        self.Pin=""
        self.Menu()
    def Menu(self):
        while(True):
            inp=int(input("""
        Welcome to Atm,Enter your choice 
        1.Enter 1 for Create Pin
        2.Enter 2 for Check Balance
        3.Enter 3 for Diposite
        4.Enter 4 for Withrwal
        5.Enter 5 for Exit
        """))
        if inp==1:
            self.Create_pin()
        elif inp==2:
            self.Ckk_blnc()
        elif inp==3:
            self.dip()
        elif inp==4:
            self.withdrawl()
        else:
            print("bye")

    def Create_pin(self):
        self.Pin = int(input("Enter your new Pin "))
        print("Pin Succesfully set")
    def Ckk_blnc(self):
        temp=input("Enter your pin")
        if temp==self.Pin:
            print(self.Balance)
        else:print("Invalid Pin")
    def dip(self):
        temp=input("Enter your Pin")
        if temp==self.Pin:
            Amount=int(input("Enter your Amount"))
            self.Balance=self.Balance+Amount
            print("Amount Succesfully Added")
        else:
            print("Invalid Pin")
    def withdrawl(self):
        temp=input("enter your pin")
        if temp==self.Pin:
            Amount=int(input("enter Amount to Withrawl"))
            if Amount<=self.Balance:
                self.Balance=self.Balance-Amount
                print("Operation succecsfull")
            else:
                print("Insufficient Balance")
        else:
            print("Invalid Pin")
    def exit(self):
        print("bye")

sbi=Atm()