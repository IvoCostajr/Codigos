cont=0
qutNum=0
while(cont<5):
    num=int(input("informe"))
    if(num%2==0 and num>0):
        qutNum+=1
    cont+=1
print(qutNum)
