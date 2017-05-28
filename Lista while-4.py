cont=0
num1=0
num=0
condica=True
while(condica):
    num=int(input("informe"))
    if(num==100):
        condica=False
    elif(num%2==0):
        num1+=num
        cont+=1
if(num1==0):
    print("não tem par")
        
print(num1/cont)

print(cont)
    
