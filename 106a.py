su,b1=list(map(str,input().split()))
lis=list(map(int,input().split()))
c1=0
for i in lis:
    if (i%2!=0):
        c1+=1
        if(c1==int(b1)):
            print(i)
