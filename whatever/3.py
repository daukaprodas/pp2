n=int(input())
r=2*n-1//2
d=r+1
for i in range(n):
    for j in range(0,r):
        print(" ",end="")
    for k in range(d,2*n-1):
        print(" ",end="")
    for l in range(r,d):
        print("*",end="")
    r-=1
    d+=1
    print()