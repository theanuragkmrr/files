numbers=["3","34","64"]
# numbers =list(map(int,numbers))
# print(numbers[2])
# from functools import reduce
# ls=[1,2,3,4]
# num=reduce(lambda x,y:x+y,ls)
# print(num)
# ============MAping========
# for i in range(len(numbers)):
#     numbers[i]=int(numbers[i])
# numbers[1]=numbers[1]+1
# print(numbers[1])
# def sqr(x):
#     return x*x
# square=list(map(sqr,ls))
# print(square)
# def convert(x):
#         for i in range(len(numbers)):
#             numbers[i] = int(numbers[i])
#         # return numbers
# p=list(map(convert,numbers))
# print(numbers[2]+1)
# sqaure=list(map(sqr,numbers))
# print(sqaure)
# ------------------filter------------------------
def greater(g):
    return g>2
ls=[1,2,3,4,5]
greaterthan=filter(greater,ls)
print(list(greaterthan))