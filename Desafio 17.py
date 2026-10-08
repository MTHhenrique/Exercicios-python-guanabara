# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa

import math

oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = math.sqrt(oposto ** 2 + adjacente ** 2)

print(f'O comprimento da hipotenusa é {hipotenusa}')