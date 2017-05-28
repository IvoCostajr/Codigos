def testaVogal(a):
    if(a=="a"or a=="e" or a=="i" or a=="o" or a=="u"):
        return True
    elif(a=="A"or a=="E" or a=="I" or a=="O" or a=="U"):
        return True
    else:
        return False

print(testaVogal("A"))
print(testaVogal("o"))
print(testaVogal("G"))
print(testaVogal("5"))
