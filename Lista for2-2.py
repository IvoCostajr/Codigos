peca=7
quilo=5
seco=3.50
totalLavagem=0
lavagemSeco=0
lavagem= int(input("Quantas lavagens deseja cadastrar?"))
for i in range(lavagem):
    tipoLavagem= (input("Tipo de lavagem? peças/quilo"))
    if(tipoLavagem=="peças"):
        lSeco= (input("Deseja lavagem à seco? s/n"))
        if(lSeco=="s"):
            qutPeca=int(input("Quantidade de peças"))
            calc1= (qutPeca*peca)+seco
            totalLavagem+= calc1
            lavagemSeco+= 1
            print ("preço lavagem por peça à seco R$",calc1)
        else:
            qutPeca1=int(input("Quantidade de peças"))
            calc2= qutPeca1*peca
            totalLavagem+=calc2
            print ("preço lavagem por peça sem opção à seco R$",calc2)
    else:
        lSeco1= (input("Deseja lavagem à seco? s/n"))
        if(lSeco1=="s"):
            qutKg= int(input("Qut quilo"))
            calc3= (qutKg*quilo)+seco
            totalLavagem+= calc3
            lavagemSeco+= 1
            print ("preço lavagem por quilo à seco R$",calc3)
                                
        else:
            qutKg1= int(input("qut quilo"))
            calc4= qutKg1*quilo
            totalLavagem+= calc4
            print ("preço lavagem por quilo sem opçãoà seco R$",calc4)
print ("Quantidade de lavagem à seco R$",lavagemSeco)
print ("Total arrecadado R$",totalLavagem)
                                            
                                
                            
