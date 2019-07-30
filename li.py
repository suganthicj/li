    
x11=int(input())
y11=""
for i in range(2,x11):
    if x11%i==0:
        flag=0
        break
    else:
        flag=1
if flag==0:
    print("yes")
else:
    print("no")
