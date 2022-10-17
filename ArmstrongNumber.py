n=int(input("Enter the no="))
sum=0
temp=n
while(n!=0):
    r=n%10
    sum=sum+r**3
    n=n//10
if(sum==temp):
    print("Armstrong No",temp)
else:
    print("Not Armstrong No",temp)
