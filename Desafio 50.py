# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0

for c in range(1, 7):
    digitado = int(input('Digite um número: '))

    n = digitado % 2

    if n == 0:
        soma += digitado

print(f'A soma deu: {soma}')