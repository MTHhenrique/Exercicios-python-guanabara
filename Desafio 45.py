# Crie um programa que faça o computador jogar Jokenpô com você

import random

print('''\nEscolha sua jogada:
[1] Pedra
[2] Papel
[3] Tesoura''')

jogador = int(input('Qual é a sua jogada? '))
computador = random.randint(1, 3)

if jogador == 1:
    print('Você escolheu PEDRA!')
elif jogador == 2:
    print('Você escolheu PAPEL!')
elif jogador == 3:
    print('Você escolheu TESOURA!')
else:
    print('Você digitou uma opção inválida!')

if jogador >= 1 and jogador <= 3:
    if computador == 1:
        print('O computador escolheu PEDRA!')
    elif computador == 2:
        print('O computador escolheu PAPEL!')
    elif computador == 3:
        print('O computador escolheu TESOURA!')

    if jogador == computador:
        print('EMPATE!')

    elif jogador == 1 and computador == 3 or jogador == 2 and computador == 1 or jogador == 3 and computador == 2:
        print('VOCÊ VENCEU!')

    else:
        print('O COMPUTADOR VENCEU!')