# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais     ISÓSCELES: dois lados iguais, um diferente    ESCALENO: todos os lados diferentes 

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if ((r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2)):

    print('Os segmentos acima podem formar um triângulo!')

    if ((r1 == r2) and (r2 == r3)):
        print('O triângulo formado será equilátero!')

    elif ((r1 == r2) or (r1 == r3) or (r2 == r3)):
        print('O triângulo formado será isósceles!')

    else:
        print('O triângulo formado será escaleno!')

else:
    print('Os segmentos acima não podem formar um triângulo!')