
def factorial(n):
    if n==0 or n==1:
        return 1
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
r=int(input("Give factoria number:"))
res=factorial(r)
print(res)       
