def facto(n):
    fact=1
    for i in range(n):
        fact=fact*(i+1)
    return fact
num=int(input("enter number to find factorial "))

def factorial_rec(n):
    if n==1 or n==0:
        return 1
    return n*factorial_rec(n-1)

# factorial=facto(num)
# print(factorial)
f=factorial_rec(num)
print(f)


