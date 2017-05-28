
n3=0
edit=int(input("Quantos pares deseja cadastrar?"))
for i in range(edit):
         n1=int(input("Digite o primeiro número"))
         n2=int(input("Digite o segundo número"))
         if(n1>n2):
             n3=n1
             n1=n2
             cont1=0
             while(n1<n3-1):
                 n1+=1
                 if(n1%4==0):
                        cont1+=1
             print(cont1)
                 
                 
         else:
              cont2=0
              while(n1<n2-1):
                  n1+=1
                  if(n1%4==0):
                        cont2+=1
              print(cont2)
         
                  
         
