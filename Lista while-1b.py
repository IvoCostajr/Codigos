#Colocar o input dentro do while
#Mudar condição de parade do while.
#Ajuste em soma dentro do if
#Print em qtdePositivos 
cont=0
qtdePositivos=0
while(cont<5):
    numero=int(input("Informe o numero"))
    if(numero>0):
        qtdePositivos+=1
    cont+=1
print(qtdePositivos)
