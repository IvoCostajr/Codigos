###Resposta Lista3-4
vip=350
cadeira=200
arquibancada=100
imposto=0.05
meia=0.5
setor=(input())
ingresso=(input())
if(setor=="arquibancada" and ingresso=="inteira"):
    print("Valor:",(imposto*arquibancada)+arquibancada)
elif(setor=="arquibancada" and ingresso=="meia"):
    mei=arquibancada*meia
    print("Valor:",(mei*imposto)+mei)
elif(setor=="cadeira" and ingresso=="inteira"):
    print("Valor:",(imposto*cadeira)+cadeira)
elif(setor=="cadeira" and ingresso=="inteira"):
    mei=cadeira*meia
    print("Valor:"(mei*imposto)+mei)
elif(setor=="vip" and ingresso=="inteira"):
    print("Valor:",(imposto*vip)+vip)
else:
    print("Você não escolheu nenhuma dasopções validas")
    
    
