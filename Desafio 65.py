# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

escolha = 's'
parada = 'n'
contagem = 0
soma = 0
numero = 0

while escolha != parada:
    numero = int(input('Digite um número: '))

    contagem += 1
    if contagem == 1:
            menor = numero
            maior = numero

    soma += numero
    media = soma / contagem

    if numero > maior:
        maior = numero

    elif numero < menor:
        menor = numero

    escolha = input('Deseja continuar[s/n]? ')

print(f'A média dos valores é {media}, o número {maior} foi o maior e o {menor} foi o menor')