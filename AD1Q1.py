import math
pi = math.pi
pi = round(pi)

print( 'Pi é ', pi)
def main():

    Kmtometro = int(input("digite o valor da entrada"))
    ResultadoEntraum = Kmtometro * 100

    KmpM = int(input("digite o valor da entrada"))
    resultadoEntradois: float = KmpM / 200 * pi * 2

    var = ResultadoEntraum / resultadoEntradois

    print(KmpM, Kmtometro, "m equivale a", resultadoEntradois, ResultadoEntraum, var, 'cm ' )
main()

número = 80000000
print('{:e}'.format(número))


numero_par = []

numero_impar = []

count = 0

while count < 1:

   x = input("Digite ")

   if x == '':

       count += 1

       continue

   num = int(x)

   if num % 2 == 0:

       numero_par.append(num)

   else:

       numero_impar.append(num)

for j in numero_impar:

   area = 3.1415*j**2

   perimetro = 2*3.1415*j

   areaArredondada = round(area, 2)

   perimetroArredondado = round(perimetro, 2)

   print(f"Área e perímetro do circulo de raio {j} são: {areaArredondada} e {perimetroArredondado}")

for n in numero_par:

   divisor = []

   for x in range(1, n +1):

      if n % x == 0:

           divisor.append(x)

   print(f"Divisores de {n} são: " + ' '.join([str(i) for i in divisor]))
