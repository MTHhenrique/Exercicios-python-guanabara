# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a porção inteira

import math
real = float(input('Digite um número real: '))
inteiro = math.trunc(real)

print('A parte inteira do número {} é {}'.format(real, inteiro))