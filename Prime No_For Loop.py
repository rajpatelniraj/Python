n=int(input("n="))
x=int(n/2)+1
for i in range(2,x):
    r=n%i
    if(r==0):
        print("Not a Prime No")
        break
    else:
        print("Its a Prime No")
