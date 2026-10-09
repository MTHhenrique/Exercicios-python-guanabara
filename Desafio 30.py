# Crie um programa que leia um numero inteiro e diga se ele é impar ou par

numero = int(input('Digite um número: '))
numero = numero % 2

if (numero == 0):
    print('O número é par')

else:
    print('o número é impar')