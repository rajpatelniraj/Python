
n,m=map(int,input().split())
s=input()
l=[[0 for i in range(m)]for j in range(n)]
flag=False
for i in range(n):
   for j in range(m):
       for c in s:
           if(c=='R'):
               if(j+1<m):
                   j+=1
               else:
                   break
           elif(c=='L'):
                if(j-1>=0):
                    j-=1
                else:
                    break
           elif(c=='F'):
                if(i+1<n):
                    i+=1
                else:
                    break
           elif(c=='B'):
                if(i-1>=0):
                    i-=1
                else:
                    break
       else:
            flag=True
            break
   if(flag):
        break
print('safe' if flag else 'unsafe')
                
