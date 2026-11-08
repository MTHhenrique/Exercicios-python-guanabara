# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

digitado = 0
soma = 0
contagem = 0
parada = 999

while not digitado == parada:
    digitado = int(input('Digite um número: '))

    if  digitado != parada:
        soma += digitado
        contagem += 1

print(f'Você digitou {contagem} número(s) e a soma deles é {soma}')