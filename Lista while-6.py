cont=0
qtFilhos=0
wi=True
while(wi):
    num=int(input("qut filhos"))
    if(num>0):
        qtFilhos+=num
        cont+=1
    else:
        wi=False
print(qtFilhos/cont)
        
