from entrada import *

listaG,listaGeralCopia,listaGeralVetores = [],[],[]
tagx,tagy,varx,vary,contadorDeLabels,contadorDeTags,linha = 0,0,0,0,0,0,0

f = open(r"saidaGerador.txt", mode = "w",  encoding="utf-8")

def listaVar(listaGeral):
  global listaGeralCopia
  for i in listaGeral:
    if(i['tipo'] == 'simples' and i['variavel'] not in listaGeralCopia):    
      listaGeralCopia.append(i['variavel'])
    elif(i['tipo'] == 'vetor' and i['variavel'] not in listaGeralVetores):
      listaGeralVetores.append(i['variavel'])

def gerador(i, contBreak):
  global listaGeralCopia,linha,contadorDeLabels 
  if contadorDeLabels == 0:       #escrever pela primeira vez com os as duas labels
    f.write(labels())
    contadorDeLabels += 1   
  linha = i
  
  if(token[linha] == 'do'):
    linha += 1
    lexema = criaLexema()
    if(contadorDeLabels != 0):
      f.write(labels())  
    f.write(" "+lexema+ '\n')
    linha += 1
    
    #ate aqui acha oq tem antes do primeiro ;
    
    lexema = criaLexema()
    salvaLista(lexema)
    f.write(labels())
    atribuicaoGerador()
    alocaMemoria()
    listaG.clear()
    
  elif(token[linha] == 'if'):
    
    f.write(labels() + " iffalse ")
    lexema = criaLexema()
    salvaLista(lexema)
    for i in range(len(listaG)):
      f.write(listaG[i])
    f.write(f" goto L{contadorDeLabels+2} \n")
    f.write(labels())
    if contBreak != 0:
      f.write(f" goto L2\n")
    else:
      atribuicaoGerador()
    listaG.clear()
  else:
    f.write(labels())
    lexema = criaLexema()
    salvaLista(lexema)
    atribuicaoGerador()
    alocaMemoria()
    listaG.clear()

def criaLexema():
  global linha
  lexema = ''
  while(token[linha] != ";"):
        lexema += token[linha] + " " 
        linha += 1  
  return lexema
    
def labels():
  global contadorDeLabels
  contadorDeLabels += 1
  return "L" + str(contadorDeLabels) + ":"

def tags():
  global contadorDeTags
  contadorDeTags += 1
  return "t" + str(contadorDeTags)

def salvaLista(lexema):
  tokenG = ''
  for i in range(len(lexema)):
    if(lexema[i] != " "):
      tokenG += lexema[i]
    else:
      listaG.append(tokenG)
      tokenG = ''
  salvaListaFinal()
  
def salvaListaFinal():
  if(listaG[0] == "while" or listaG[0] == "if"):
    del listaG[0]
    del listaG[0]
    i = 0 
    
    while(i <= len(listaG)): 
      if(i +1 <len(listaG) and listaG[i+1] == ')'):
        i += 1
        while(i <= len(listaG)):
          if(i <= len(listaG)):
            del listaG[i]
            if(i + 1 <=len(listaG)):
              i -= 1
          i +=1
      i += 1  
      
def atribuicaoGerador():
  global tagx,tagy,varx,listaGeralCopia
  contador,i = 0,0  
  while i <= len(listaG):
    if(i+1 < len(listaG)):
      if(listaG[i] == '['):
        if(i == 1):
          tagx = tags()
          varx = listaG[i-1]
          f.write(tagx + " = " + str(listaG[i+1]) + " * 8\n")
          contador = 1
        else:
          vary = listaG[i-1]
          tagy = tags()
          f.write(tagy + " = " + str(listaG[i+1]) + " * 8\n")
    i += 1  
    
def alocaMemoria(): #essa serve para criar as tags e alocar memoria
  global varx,vary,listaGeralCopia,listaGeralVetores
  lexema = ''
  i = 0
  while i <= len(listaG):
    if(i+1 < len(listaG) and listaG[i] in listaGeralCopia and listaG[i+1] == '='):     
      lexema += listaG[i] +" "+ listaG[i+1]
      if(listaG[i+3] == '['): # var simples e vetor
        lexema += " " + listaG[i+2]  + listaG[i+3] + tagy + "]"
        f.write(lexema+"\n")
        lexema = ''
      else:  #duas var simples
        var = len(listaG)
        f.write(listaG[var]+"\n")
      
    elif(i+1 < len(listaG) and listaG[i] in listaGeralVetores and i <=3):
      if(listaG[5] in listaGeralVetores):  # dois vetores 
        tagz = tags()
        f.write(str(tagz) + " = " + listaG[5] +"[" + tagy + "]\n") 
        f.write(str(varx) + "[" + tagx +"] = " + tagz + "\n")
        
      elif(listaG[5] in listaGeralCopia): #vetor e var simples
        if(listaG[4] == '='):
          f.write(varx + "[" + tagx +"] = " + listaG[5] + "\n") 
        else:
          tagz = tags()
          f.write(tagz + " = " + varx +"[" + tagx + "]\n")
          f.write("if " + str(tagz) + str(listaG[4]) + listaG[5] + " goto L" + str(contadorDeLabels - 1) + "\n"  )
    i += 1
        