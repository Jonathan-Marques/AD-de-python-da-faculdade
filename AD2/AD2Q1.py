#Subprograma
def gravaEntrada():
    lista =[]
    entrada = input()
    while entrada !="":
        lista.append (entrada)
        entrada = input()
    return lista
#Subprograma
def verificaEntrada (lista):
    numerosValidos = []
    if lista != []:
        for numeros in lista:
            try:
                if numeros != "":
                    int, float (numeros)
                    numerosValidos.append(numeros)
            except ValueError:
                continue
    print("Lista de Números válidos lidos =", numerosValidos)
    return numerosValidos
#Programa principal
entrada = gravaEntrada()
verificaEntrada(entrada)

