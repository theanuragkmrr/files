def dec(fun1):
    def nowexe():
        print("1st")
        fun1()
        print("2nd")
    return nowexe
@dec
def dec2():
    print("Anurag is good boy")
# dec2=dec(dec2)
dec2()