# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 5. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random

tentativa = int(input('De 0 a 5, em qual número você acha que o computador pensou? '))
lista = [0, 1, 2, 3, 4, 5]
computador = random.choice(lista)
contador = 1

while not computador == tentativa:
    contador += 1
    tentativa = int(input('De 0 a 5, em qual número você acha que o computador pensou? '))

print(f'Parabéns!! Você acertou, o número era {computador}. Sua quantidade de tentativas foi: {contador}')