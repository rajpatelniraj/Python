a=input()
y=int(input())
c=""
for i in a:
    for j in range(b):
        c=c+i
    if c in a:
        a=a.replace(c,"")
    c=""
print(a)
