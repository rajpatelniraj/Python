n=int(input("Enter a Number"))
temp=n
sum=0
while(n!=0):
    r=n%10
    sum=sum*10+r
    n=int(n/10)
if(temp==sum):
    print("It's a Palindrome ",temp)
else:
    print("Not a Palindrome ",temp)
