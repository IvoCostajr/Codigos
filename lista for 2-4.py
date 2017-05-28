marfim=0
eletrolux=0
brastemp=0
branco=0
preçodeco=0
objdeco=0
dados= int (input("Quantas vendas deseja cadastrar?"))
for i in range (dados):
    moveis=(input("Informe a cor dos móveis.Marfim / branco"))
    eletrodomestico=(input("Informe  a marca do eletrodomestico.Eletrolux/Brastemp"))
    decoracao=int(input("Informe se deseja informar materias de decoração.s/n"))
    if(moveis=="Marfim"):
        marfim+=1
    
    elif(moveis=="Branco"):
        branco+=1
    if(eletrodomestico=="Eletrolux"):
        eletrolux+=1
    elif(eletrodomestico=="Brastemp"):
        brastemp+=1
    if(decoracao=="s"):
        preço=int(input("Informe o preço do material de decoração")
        preçodeco+=preço
        objdeco+=1
if(marfim==0 and branco==0):
print("Nenhum movel vendido")
if(brastemp==0 and eletrolux==0)
print("nenhum eletrodomestico")
if(preçodeco==0):
print("nenhum obj de decoração")



            
    
    
