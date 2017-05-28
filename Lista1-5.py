vDesconto=0.10
valor=float(input("digite o valor da compra"))
fPagamento=(input("informe a forma de pagamento"))
if(valor>=100 and fPagamento=="dinheiro"):
    desconto=float(valor*vDesconto)
    dTotal=float(valor-desconto)
    print(dTotal)
elif(valor>100 and fPagamento=="cheque"):
    print(valor)

elif(valor<100 and fPagamento=="dinheiro" and fPagamento=="cheque"):
    print(valor)
else:
    print("Forma de pagamnrto inválida")
