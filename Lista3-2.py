###Resposta questão 2 da lista 03 comando condicionais
gasolina=2.53
etanol=2.09
diesel=1.92
tipoCombustivel=(input("Qual cmbustível desejado"))
valor=int(input("Valor a ser abastecido"))
if(tipoCombustivel=="gasolina"):
    cac=valor/gasolina
    print(cac,"Litros.Não ganhou troca de óleo")
elif(tipoCombustivel=="etanol"):
    cac1=valor/etanol
    if(cac1>30):
        print(cac1,"Litros de etanol.Ganhou troca de óleo")
    else:
        print(cac1,"Litros de etanol.Não ganhou troca de óleo")
else:
    cac2=valor/diesel
    print(cac2,"Litros de diesel.Não ganhou troca de óleo")
        
