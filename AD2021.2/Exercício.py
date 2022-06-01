def principal():
    numeropar = numeroimpar = menor = maior = qtdprimo = 0
    quantidade = 1
    while True:
        numero = int(input("digite um numero:"))
        quantidade += 1
        resultado = numero % 2
        if resultado == 0:
            numeropar +=1
        else:
            numeroimpar +=1

        if ehprimo(numero):
            qtdprimo +=1

        if quantidade == 1:
            maior = menor = numero
        else:
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero


        if numero == 0:
            break


    print("Primo: {}".format(qtdprimo))
    print("Numeros Impar {}: ".format(numeroimpar))
    print("Numeros Par {}: ".format(numeropar))
    print("Menor: {}".format(menor))
    print("Maior: {}".format(maior))


def ehprimo(numero):
    divisores = 0
    inicio = 1
    while inicio <= numero:
        if numero % inicio ==0:
            divisores +=1
        inicio +=1
    if divisores == 2:
        return True
    else:
        return False

principal()