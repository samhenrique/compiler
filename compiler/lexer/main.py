from simbolos import *

#Alunos: Samuel Henrique, Vinicius Souza, Allan Miller, João Firmino e Ariel Nunes

token = [] #adiciona os tokens.
espacobranco = ' '
lexema = '' #adiciona string por string para fazer a verificaçao.

f = open(r"test.txt", mode='r', encoding="utf-8") #abre o codigo.
codigo = f.read() #le o codigo.
codigo = codigo.replace("\t",'').replace('\n',r'\n ') # tira os tab e as quebras de linha.

def show(): #funcao principal.
    linha = 1
    salvaTokens(lexema)  
    arquivo = open('saida.txt', 'w') #cria o arquivo.
    for i in range(len(token)): #laço para imprimir os tokens no arquivo.
        if(token[i] != ''):
           tags = tag(i)
           if(tags == 257 and token[i] == 'int'):
                arquivo.write(f'Token: {{\'tag\': {tags}, \'lexeme\': \'{token[i]}\', \'width\': 4, \'line\': {linha}}}\n')
           elif(tags == 257 and token[i] == 'float'):
                arquivo.write(f'Token: {{\'tag\': {tags}, \'lexeme\': \'{token[i]}\', \'width\': 8, \'line\': {linha}}}\n')
           elif(tags == 263 or tags == 264 or tags ==275 or tags == 258 or tags == 259 or tags == 265 or tags == 274):
                arquivo.write(f'Token: {{\'tag\': {tags}, \'lexeme\': \'{token[i]}\', \'line\': {linha}}}\n')
           elif(tags == 0):
                arquivo.write(f'Token: {{\'tag\': \'{token[i]}\', \'line\': {linha}}} \n')
           elif(tags == 270):
                arquivo.write(f'Token: {{\'tag\': {tags}, \'value\': \'{token[i]}\', \'line\': {linha}}}\n')
           elif(tags == 222):
                linha += 1
    
    arquivo.close()#fecha o arquivo.
  
def tag(i): # atribui um codigo a cada token.
    listadechar = ['a','b','c','d','e','f','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']      
    if (token[i] == 'int' or token[i] == "float"):
        return  257
    elif(token[i] in listadechar):
        return  264
    elif(token[i].isdigit()):
        return  270 
    elif(token[i] == "break"):
        return 258       
    elif(token[i] == "do"):
        return 259 
    elif(token[i] == "if"):
        return 265 
    elif(token[i] == "while"):
        return 275
    elif(token[i] == ">="):
        return 263 
    elif(token[i] == "true"):
        return 274 
    elif(token[i] == r"\n"):
        return 222
    elif(token[i] == ' '):
        pass
    else:
        return 0             

def salvaTokens(lexema):
  for i in range (len(codigo)):  #percorrre todo o codigo.
      if (codigo[i] != espacobranco):
          lexema += codigo[i] # adiciona um char por vez no lexema.
    
      if (i+1 < len(codigo) and codigo[i]+codigo[i+1] in outros_simbolos): #verifica operadores com mais de um caractere.
            lexema += codigo[i+1]
            token.append(lexema)
            lexema =''
               
      elif (i+1 < len(codigo)): # previnir erro de index out of range.
          if codigo[i+1] == espacobranco or lexema in palavrasChave : # se o proximo char == ' ' ou o lexema formado é uma palavra chave.
            if codigo[i-1] in operadores: #verifica se o lexema faz parte de um operador de um caractere.
              lexema = ''        
            else: 
              token.append(lexema)
              lexema = ''
          elif (codigo[i+1] in palavrasChave and codigo[i] != espacobranco): #se o proximo char for um simbolo.
            token.append(lexema)
            lexema = ''
            
      else: #ultimo token.
        lexema = codigo[i]
        token.append(lexema) 

show()
