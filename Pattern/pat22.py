n=int(input("n="))
for  i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(97+n-i),end=" ")
    print()