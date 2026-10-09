# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuario venceu ou perdeu

import random

tentativa = int(input('De 0 a 5, em qual número você acha que o computador pensou? '))
lista = [0, 1, 2, 3, 4, 5]
computador = random.choice(lista)

if (computador == tentativa):
    print(f'Parabéns!! Você acertou, o número era {computador}.')

else:
    print(f'ERROU!!! O número era {computador}.')