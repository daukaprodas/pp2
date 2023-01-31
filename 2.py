x=int(input())
c=int(input())
v=int(input())
if x>c and c>v:
    print(v)
elif(v>x and x>c):
    print(c)
else:
    print(x)
