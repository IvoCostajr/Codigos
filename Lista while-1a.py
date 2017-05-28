#Criar variavel soma
#Igualar a condição if igual a zero para com seja contabilizado numeros pares.
#Mudar condição de parada do while.
cont=0
soma=0
while(cont<5):
    numero=int(input("Informar o número"))
    if(numero%2==0):
        soma+=numero
    cont+=1
print(soma)
        
