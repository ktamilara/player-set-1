n1=int(input())
rem1=0
while n1!=0:
  temp1=n1%10
  rem1=(rem1*10)+temp1
  n1=n1//10
print(rem1)
