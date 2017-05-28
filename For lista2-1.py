cont1=0
cont2=0
vMedio=0
mValor=0
desc=0
an=0
for i in range(3):
    descricao=(input("descrição"))
    valor=int(input("valor obj"))
    ano=int(input("ano obj"))
    if(ano<1827):
            cont1+=1
            vMedio+=valor
            if(valor>mValor):
                mValor=valor
                desc=descricao
                an=ano
    else:
            vMedio+=valor
            if(valor>mValor):
                mValor=valor
                desc=descricao
                an=ano
    cont2+=1
print(cont1,"obj antes de 1827")
print(vMedio/cont2,"valor medio")
print("obj mais valioso",desc,"do ano",an)


