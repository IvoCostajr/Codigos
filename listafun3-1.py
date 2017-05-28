pTotal=0
pTotal1=0
pTotal2=0

def calculaCondominio(nome,dias):
   
    if(nome=="duna"or nome=="Duna"):
        cac=0.02*dias
        vixi=300*cac
        pTotal=300+vixi
        return pTotal
    elif(nome=="chateau"or nome=="Chateau"):
            cac1=0.04*dias
            vixi1=300*cac1
            pTotal1=300+vixi1
            return pTotal1
    else:
        cac2=0.03*dias
        vixi2=220*cac2
        pTotal2=220+vixi2
        
        return pTotal2
print("Duna devera pagar o total de R$",calculaCondominio("duna",0))
print( "Chateau devera pagar o total de R$",calculaCondominio("Duna",2))
print("Petit devera pagar o total de R$",calculaCondominio("Petit",6))
        
