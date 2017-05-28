pBus= 350
pVan= 200
cpBus= 42
cpVan= 20

qutPessoas= int(input("Iquantidade de pessoas: "))
qutBus= qutPessoas//cpBus
rBus= qutPessoas%cpBus
qutVan= rBus//cpVan
rVan= rBus%cpVan

if rVan > 0:
    qutVan= qutVan + 1
    vBus= qutBus*pBus
    vVan= qutVan*pVan
    vTotal= vBus+vVan
    vPessoa= vTotal/qutPessoas
print("Quantidade de onibus locados ", qutBus)
print("Quantidade de vans locadas: ", qutVan)
print("O valor total do excurssão é: R$ %.2f"% vTotal)
print("O valor individual é: R$ %.2f"% vPessoa)
