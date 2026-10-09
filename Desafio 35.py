# Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou não formar um triangulo

a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))

if (a + b > c and a + c > b and b + c > a):
    print(f'As três retas conseguem formar um triângulo')

else :
    print(f'As três retas não conseguem formar um triângulo')