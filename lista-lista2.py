a=[]

for  i in range (5):
    num=int(input())
    a.append (num)
c=a[0]
for i in range(len (a)):
    if(a[i]<c):
        c=a[i]
print(c)

    

