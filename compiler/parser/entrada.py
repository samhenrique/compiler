import re

f = open(r"entrada.txt", mode = "r",  encoding="utf-8")
codigo = f.read()

comp = re.compile(r"Token: \{'tag': \d{3}, 'lexeme': '([a-zA-Z]+)', 'width': \d, 'line': (\d)\}|Token: \{'tag': \d{3}, 'value': '(\d|\d\d\d)', 'line': (\d)\}|Token: \{'tag': \d{3}, 'lexeme': '([a-zA-Z]+|[^']*)', 'line': (\d)\}|Token: \{'tag': '(.)', 'line': (\d)\}")
resultado = re.findall(comp, codigo)

token = []
linha = []

for j in range(len(resultado)):
    if resultado[j][0] != '':
        token.append(resultado[j][0])
        linha.append(resultado[j][1])
    elif resultado[j][2] != '':
        token.append(resultado[j][2])
        linha.append(resultado[j][3])
    elif resultado[j][4] != '':
        token.append(resultado[j][4])
        linha.append(resultado[j][5])
    elif resultado[j][6] != '':
        token.append(resultado[j][6])
        linha.append(resultado[j][7])
