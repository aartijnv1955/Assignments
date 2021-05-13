n=int(input())
a=[int(input()) for i in range(n)]
r=a[::1]
for i in r:
    print(i)