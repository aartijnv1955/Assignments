n=int(input("enter a nmber:"))
def isprime(n):
    if (n<2):
        return False
    for i in range(2,n//2):
        if n%i==0:
            return False
    return True
if isprime(n):
    print(str(n) +"is a prime number")
else:
    print(str(n) +"is not a prime number")