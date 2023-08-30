# list=["ghapaghap","Anurag","Oyo","Anshika"]
# i=1
# for item in list:
#     if i%2 == 0:
#         print(f"BF GF hai {item}")
#     i+=1
sum=0
while True:

    num=input("Enter price: \n")

    if (num!="q"):

        sum=sum+int(num)
    else:
        
        print("Your bill is:", sum)
        break