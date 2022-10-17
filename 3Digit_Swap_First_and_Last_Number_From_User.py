x=int(input("Enter 3Digit Number="))
a=x%10*100
x=x//10
x=a+x%10*10+x//10
print("x=",x)
