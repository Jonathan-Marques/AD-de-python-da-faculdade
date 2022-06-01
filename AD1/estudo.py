# Subprogramas
def converte(numDecimal, base):
    numConvertido = ""
    while numDecimal >= base:
        numConvertido = str(numDecimal % base) + numConvertido
        numDecimal = numDecimal // base
        numConvertido = str(numDecimal) + numConvertido
    return numConvertido
# Programa Principal
num = int(input())
while num != -1:
    for b in range(2, 10):
        print(converte(num, b), end=" ")
        print()
    num = int(input())