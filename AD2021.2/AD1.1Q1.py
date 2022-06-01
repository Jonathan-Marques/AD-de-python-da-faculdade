import math

numero = 1
while numero:
    try:
        numero = int(input("Digite um numero:"))
        resultado = numero % 2
    except ValueError as ve:
        if numero:
            break

    if resultado == 0:
        divisores = [i for i in range(1, numero + 1) if numero % i == 0]
        print("Divisores de {} são: ".format(numero), divisores)

    else:
        area = math.pi * math.pow(numero, 2)
        area = round(area, 2)
        perimetro = 2 * math.pi * numero
        perimetro = round(perimetro, 2)
        print("Área e Perímetro do Círculo de Raio {} são: ".format(numero), area, "e", perimetro)
