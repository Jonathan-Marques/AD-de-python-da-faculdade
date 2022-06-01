
soma = media = menor = maior = 0
quantidade = 1
while True:
    numero = int(input("digite um numero:"))
    soma += numero
    quantidade += 1
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    if numero == 0:
        break

media = soma / quantidade
media = round(media, 2)
print("Soma: {}".format(soma))
print("Média: {}".format(media))
print("Menor: {}".format(menor))
print("Maior: {}".format(maior))

