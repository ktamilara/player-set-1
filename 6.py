x,y=input().split()
z=[]
if(len(x)!=len(y)):
    print("no")
else:
    for j in range(len(x)):
        if x[j] in z:
            continue
        else:
            y=y.replace(y[j],x[j])
            z.append(x1[j])
    if y==x:
        print("yes")
    else:
        print("no")
