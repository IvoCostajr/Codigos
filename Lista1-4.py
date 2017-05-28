numero=int(input())
if(numero%2==0 and numero%3==0 and 102%numero==0):
    print("Numero não é impar")
    print("Numero é multiplo de 3")
    print("Numero é divisor de 102")
elif(numero%2!=0 and numero%3==0 and 102%numero==0):
    print("Numero é impar")
    print("Numero é multiplo de 3")
    print("Numero é divisor de 102")
elif(numero%2==0 and numero%3!=0 and 102%numero==0):
    print("Numero não impar")
    print("Numero não multiplo de 3")
    print("Numero é divisor de 102")
elif(numero%2!=0 and numero%3==0 and 102%numero!=0):
    print("Numero é impar")
    print("Numero é multiplo de 3")
    print("Numero não é divisor de 102")
else:
    print("Numero não impar")
    print("Numero não é multiplo de 3")
    print("Numero não é divisor de 102")
    


