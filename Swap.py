n=int(input())
sum=0
i=100
rem=n%10
sum+=(rem*i)
n//=10
rem=n%10
sum+=(rem*10)
n//=10
rem=n%10
sum+=(rem*1)
print(sum)
