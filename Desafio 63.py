# Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8 

n = int(input('Quantos termos você quer mostrar? '))

a = 0
b = 1
contador = 0

while contador < n:
    print(a, end=' → ')
    proximo = a + b
    a = b
    b = proximo
    contador += 1

print('FIM')