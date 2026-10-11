# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

nascimento = int(input('Qual seu ano de nascimento? '))
idade = 2026 - nascimento

if (idade == 18):
    print('Está na hora de se alistar!!')

elif (idade > 18):
    tempo = idade - 18
    print(f'Você já deveria ter se alistado a {tempo} ano(s), mas ainda dá tempo!!')

else:
    tempo = 18 - idade
    print(f'Você não tem idade o suficiente para se alistar, ainda falta {tempo} ano(s)')