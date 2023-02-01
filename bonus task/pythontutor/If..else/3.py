n=int(input())
m=int(input())
l=int(input())
p=int(input())
if n%2==m%2 and l%2==p%2:
    print("YES")
elif n%2==p%2 and l%2==m%2:
    print("YES")
elif n%2==l%2 and p%2==m%2:
    print("YES")
else: 
    print("NO")
