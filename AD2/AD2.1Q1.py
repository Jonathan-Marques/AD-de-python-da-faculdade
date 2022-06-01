"""def lerArquivo ():
    entrada = input()
    with open (entrada, "r") as arquivo:
        matriz = arquivo.readlines()
    return matriz

matriz = lerArquivo()
print("", matriz)"""

arquivo = open('testeAD2Q1.txt','r')

matriz = []

linha = arquivo.readline()
while linha!= "":
    elementos = linha.split()
    for n in range(len (elementos)):
        elementos[n] = int(elementos[n])
    matriz.append(elementos)

    linha = arquivo.readline()

print(matriz)