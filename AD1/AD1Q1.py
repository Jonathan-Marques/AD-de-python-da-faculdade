# AD1 - Questão 1


# Programa Principal

valor= input()
if valor !="":
    quantidade = float(valor.split()[0])
    preco = float(valor.split()[1])
    gasto = quantidade * preco
    totalGasto = gasto
    itens = 1
    menor = preco
    maior = preco

    quantidade = float(valor.split()[0])
    preco = float (valor.split()[0])

    if menor > preco:
        menor = preco
    elif maior < preco:
        maior = preco
    print("Item de menor preço:",  menor)
    print("Item de maior Preço:",  maior)
    print("Itens comprados:", itens)
    print("Total gasto:",  totalGasto)
else:
    print("Nenhum produto foi comprado!:", )