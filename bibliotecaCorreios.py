

def validaTipoItem(item):
   if type(item) is str:
      item = item.lower()
   if item == "documento" or item == "pacote":
      return True
   else:
      return False

def validaPeso(peso):
   if peso >= 0:
      return True
   else:
      return False

def convertePesoQuiloPraGrama(peso):
   return peso * 1000

def convertePesoGramaPraQuilo(peso):
   return peso / 1000


def calculaCustoItem(tipo, peso):
   valorTipo = 0
   if tipo.lower() == "pacote":
      valorTipo = 3
   else:
      valorTipo = 2
   return valorTipo * convertePesoGramaPraQuilo(peso)
   
def validaEmbalagem(tipo):
   if type(tipo) is str:
      tipo = tipo.lower()
   if tipo == "pequena" or tipo == "média" or tipo == "grande":
      return True
   else:
      return False

def calculaCustoEmbalagem(tipo):
   if tipo.lower() == "pequena" or tipo.lower() == "p":
      return 4
   elif tipo.lower() == "média" or tipo.lower() == "m":
      return 7
   elif tipo.lower() == "grande" or tipo.lower() == "g":
      return 10


def validaEntrega(tipo):
   if type(tipo) is str:
      tipo = tipo.lower()
   if tipo == "normal" or tipo == "sedex" or tipo == "sedex10":
      return True
   else:
      return False

def calculaCustoEmentrega(tipo):
   if tipo.lower() == "normal":
      return 0
   elif tipo.lower() == "sedex":
      return 5
   elif tipo.lower() == "sedex10":
      return 8



   
