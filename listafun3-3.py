def calculaComissao(a):
    qutcomissao=a*0.07
    precot=(80*qutcomissao)
    return   "%.1f" % precot
def calculaBonus(a):
    if(a>50):
        bonus=70
        return bonus
    else:
        return 0
print(calculaComissao(0))
print(calculaComissao(1))
print(calculaComissao(5))
print(calculaComissao(10))
print(calculaBonus(0))
print(calculaBonus(15))
print(calculaBonus(50))
print(calculaBonus(62))
print(calculaBonus(130))


