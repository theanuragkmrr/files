def fun(*data):
    for item in data:
        if len(data)==3:
            print(f"Name is {data[0]} ,age is {data[1]} and Gender is {data[2]}")
            break
        elif len(data)==2:
            print(f"Name is {data[0]} and age is {data[1]}")
            break
        else:
            print(f"Name is {data[0]}")
            break

lis=["Anurag",22,"Male"]
lis=["Keshav",23,"Male"]
fun(*lis)
# ----------------------**kwargs------------------------------------------
def fun2(**dat):
    for key, value in dat.items():
        print(key,value)

dic={"Anurag":22,"Manan":23,"Sumit":22,"Ajay":22,"Keshav":23,"Nishant":23}
fun2(**dic)


# def addn(*args):
#     total=sum(args)
#     print(total)
# addn(2,3)
# addn(4,5,6)

