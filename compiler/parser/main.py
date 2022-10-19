#Alunos: Samuel Henrique, Vinicius Souza, Allan Miller, João Firmino e Ariel Nunes
from tabelaDeSimbolos import *
from entrada import *
from geradorDeCodigo import *

comparacoes = ['==','!=','<','>','<=','>=']
operacoes = ['+','-','*','/']
vetores = []
contadorChave = 0
contBreak = 0
i = 0 
x = 0
escopo = 0
listaGeral = []
 
def proximo():
  global i
  i += 1

def erro():
  global i
  print(f'na linha {linha[i]}')
  i += 1
  exit()
  return 0

def erroDeDigitacao():
  global i
  if(token[i] not in palavrasReservadas and token[i] not in comparacoes and token[i] not in vetores and token[i] not in operacoes and variavelCriada(i) == 0):
    print("erro de digitação ", end="")
    erro()


def verWhile():
  global i
  if(token[i] == 'while'):
     proximo()
     if(token[i] == "("):
       proximo()
       if(verCondicao()):
         proximo()
         if(token[i] == ")"):
           proximo()
           print("sucesso while")
           return 1
  else:
    print("erro no while ", end="")
    erro()

def verCondicao():
    global i
    if(token[i] == 'true'): 
      return 1
    elif(token[i] == 'false'):
      return 1
    elif(verComparacao()):
      return 1
    else:
      print("condição incompatível")
      erro()

def verComparacao():
  global i
  if(vetor() or variavelCriada(i)):
    proximo()
    if(token[i] in comparacoes):
       proximo()
       if(vetor() or variavelCriada(i)):
         return 1
  else:
    print("comparação incompatível ", end="")
    erro()
    
def ehVetor():
  global i
  for j in variaveis:
    if(token[i] == j["variavel"] and j['tipo'] == 'vetor'):
      return 1

def vetor():  #quando achar uma variavel do tipo vetor ele vai ver se os proximos tokens se comportam realmente como uma variavel do tipo vetor
   global i
   lexema = ''
   if(ehVetor()):
     lexema += token[i]
     proximo()
     if(token[i] == '['):
        lexema += token[i]
        proximo()
        if(variavelCriada(i) or token[i] in possiveisPosicoes):   # todas as posocoes possiveis do vetor
          lexema += token[i]
          i +=1
          if(token[i] == ']'):
             lexema += token[i]
             vetores.append(lexema)             
             return 1
   else:
      
      return 0

  
def verIf(): #mesma função do while kkkk
  global i
  if(token[i] == 'if'):
     proximo()
     if(token[i] == "("):
       proximo()
       if(verCondicao()):
         proximo()
         if(token[i] == ")"):
          proximo()
          if(atribuicao()):
            print("sucesso if c break")
            proximo()
            if(token[i] == "else"):
              proximo()
              if(token[i] == "{"):
                proximo()
                if(atribuicao()):
                  proximo()
                  if(token[i] == "}"):
                    print("sucesso else")
                    proximo()
                    return 1
            else:
              return 1
     else:
       print("erro no if ", end='')
       erro()
  else:
    return 0   

def verDoWhile():
   global i 
   if(token[i] == 'do'):
     proximo()
     if(atribuicao()):
      if(verWhile()): 
          proximo()  
          print('sucesso do while')          
          return 1
      else:
        print("erro no do while")
        erro()
        
def atribuicao():
  global i
  global contBreak
  if(vetor() or variavelCriada(i)):
     proximo()
     if(token[i] == '='):
       proximo() 
       if(vetor() or variavelCriada(i)):
         proximo()
         if(token[i] == ';' or stmt()):
           print("sucesso atribuicao")
           return 1         
  elif(token[i] == "break"):
    contBreak += 1
    return 1
  else:
    print("atribuição incompatível ", end="")
    erro()
    return 0         
          
def stmt():
  global i
  if(token[i] in operacoes):
    proximo()
    if(converteInt(token[i]) or variavelCriada(i) or vetor()):
      proximo()
      if(token[i] == ';'):
        proximo()            
        return 1
  else:
    print("incapaz de operar ", end="")
    erro()
    return 0

def block(): 
  global contadorChave
  global i
  global escopo
  if(token[i] == "{"):
    contadorChave += 1
    escopo += 1
    proximo() 
    
  elif(token[i] == "}"):
    contadorChave -= 1
    proximo() 

  if(contadorChave == 0):   
    print("sucesso chave")
      
def verEstruturas():
  global x
  global i
  global contadorChave
  global contadorQuebra
  global escopo
  global contBreak
  l = 0
  
  for l in range(len(token)):
    if(i < len(token)):
       if(token[i] == 'while'):
         x = i 
         verWhile()
       elif(token[i] == "int" or token[i] == "float"):
         if not(verVariavel(i,escopo)):
            erro()          
         i = auxx()
       elif(token[i] == 'do'):
         x = i  
         if(verDoWhile()):
          listaVar(variaveis)
          gerador(x, contBreak)
            
       elif(token[i] == 'if'):
         x = i
         if(verIf() and contBreak != 0):
           listaVar(variaveis)
           gerador(x, contBreak)
           contBreak == 0
         elif(verIf() and contBreak == 0):
           listaVar(variaveis)
           gerador(x, contBreak)
    
       elif(variavelCriada(i) or token[i] in vetores) :
         x = i
         if(atribuicao()):
           listaVar(variaveis)
           gerador(x, contBreak)
           
       elif(token[i] == "{" or token[i] == "}"):
         block()
       elif(token[i] == ";"):
         proximo()
       else:
         erroDeDigitacao()
         i += 1 
if(block() == 0):
  print(f"erro de chaves na linha {linha[i]}")

verEstruturas()
f.write("goto L1\n")
f.write("L2:")
f.close()
 

  

