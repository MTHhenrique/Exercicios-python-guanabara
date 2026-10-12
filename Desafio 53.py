# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
# APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.


frase = input('Digite uma frase: ').upper().replace(' ', '')

inverso = frase[::-1]

if frase == inverso:
    print('Temos um palíndromo!')
else:
    print('Não é um palíndromo!')
