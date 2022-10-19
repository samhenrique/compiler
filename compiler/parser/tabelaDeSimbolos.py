#tabela de símbolos
from entrada import *
palavrasReservadas = ['int','while','do','if','float',';']
variaveis = []
aux = 0
numero = 0
possiveisPosicoes = []
vetores = []

def verVariavel(i,escopo):
   global aux
   global numero
   aux = i
   if(token[aux] == 'int' or token[aux] == 'float'):
      aux = aux +1
      if((token[aux] not in palavrasReservadas) and procurarVariavel(escopo)):
         if(token[aux] != '['):
            if(token[aux + 1] == ';'):
               variaveis.append({"variavel":token[aux], "escopo":escopo, 'tipo': 'simples','valor': 0})              
               print("sucesso variável") # só pra ver se deu certo 
               aux = aux + 1           
               return 1
         else: 
            aux = aux +1
            if(converteInt(token[aux])):
               numero = int(token[aux])
               aux = aux +1
               if(token[aux]==']'):
                  aux = aux + 1
                  if(token[aux + 1] == ';'):       
                     variaveis.append({"variavel":token[aux], "escopo":escopo, 'tipo': 'vetor','valor': 0})
                     posicoesDeVetorValidas()
                     aux = aux +1
                     print("sucesso variável") # só pra ver se deu certo
                     return 1
      else:        
         return 0


def auxx():
  global aux
  return aux
  
def procurarVariavel(escopo):
  global aux
  if(len(variaveis) == 0):
    return 1
  else:
    for j in variaveis:
      if(j['variavel'] == token[aux] and j['escopo'] == escopo):
        print("variável já declarada")
        return 0      
    return 1 

def converteInt(token): #essa função vê se oq foi declarado dentro de vetor é realmente um inteiro.  
  if(token.isnumeric()): 
     return 1 
  else:
     return 0  

def posicoesDeVetorValidas(): #controla os valores possiveis de memoria que eu posso acessar num vetor
  global numero
  for k in range(numero):
    possiveisPosicoes.append(str(k)) 
  numero = 0
       
def variavelCriada(i):
  global aux
  aux = i
  for j in variaveis:
    if(token[aux] == j["variavel"]):
        return 1
  return 0

def ehVetor(i):
  global aux
  aux = i
  for j in variaveis:
    if(token[aux] == j["variavel"] and j['tipo'] == 'vetor'):
      return 1

def lookFor(i,escopo): # procura por varievis nos escopo mais interno
  global aux
  aux = i
  for j in reversed(range(escopo)):
    for k in variaveis:
       if(token[aux] == k['variavel'] and k['escopo'] == j):
          return k
         
    

  

