

import bibliotecaCorreios

tipoItem = input("Que tipo de arquivo você deseja enviar?")
peso = float(input("Digite o peso da encomenda:"))
embalagem = input("Qual embalagem você deseja utilizar?")
tipoEntrega = input("Que tipo de entrega você deseja?")

custo = 0

if bibliotecaCorreios.validaTipoItem(tipoItem)  == True and bibliotecaCorreios.validaPeso(peso) == True:
   custo += bibliotecaCorreios.calculaCustoItem(tipoItem,peso)
if bibliotecaCorreios.validaEmbalagem(embalagem) == True:
   custo += bibliotecaCorreios.calculaCustoEmbalagem(embalagem)
if bibliotecaCorreios.validaEntrega(tipoEntrega) == True:
   custo += bibliotecaCorreios.calculaCustoEmentrega(tipoEntrega)

print(custo)
