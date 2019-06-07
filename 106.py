n1,k1=map(int,input().split())
l1=list(map(int,input().split()))
a2=[]
for x in range(len(l)):
	if(l[x]%2!=0):
		a2.append(l[x])
print(a2[k1-1])
