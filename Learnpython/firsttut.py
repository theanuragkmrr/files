# print("enter number of rows: ")
# rows=int(input())
# print("type 1 or 0")
# boolv=int(input())
# two=bool(boolv)
# if boolv==True:
#     for i in range(1,rows+1):
#         for j in range(1,i+1):
#             print("*",end=" ")
#         print()
# def fun1(a,b,c,d,t):
#     print(a,b,c,d,t)

# def funagrs(*args):
#     # print(type(args))
#     for i in args:
#         print(i)
#
# # fun1("harry","h","anurag","anshika","girl")
# har=["harry","h","anurag","anshika","girl"]
# funagrs(*har)
# def dict(normal,**args):
# *args,**kwars
#     print(normal)
#     print(type(args))
#     for key,value in args.items():
#         print(f"{key} is a boyfreind of {value}")
#
# normal="Sabka katega"
# dic={"Anurag":"Anshika","Shivam":"priya","Manan":"Ajay"}
# dict(normal,**dic)
# list=["ghapaghap","Anurag","Oyo","Anshika"]
# i=1
# # for item in list:
# #     if i%2 == 0:
# #         print(f"BF GF hai {item}")
# #     i+=1
# for index,item in enumerate(list):
#     if index%2!=0:
#         print(f"BF GF hai {item}")
# import sklearn as sk
# print(sk.__version__))