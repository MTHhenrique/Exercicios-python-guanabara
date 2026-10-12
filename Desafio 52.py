# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. 


numero = int(input('Digite um número inteiro: '))
total = 0

for c in range(1, numero + 1):
    if numero % c == 0:
        total += 1

if total == 2:
    print('É um número primo!')
else:
    print('Não é um número primo!')