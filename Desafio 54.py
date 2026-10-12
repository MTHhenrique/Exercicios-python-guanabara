# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

maiores = 0
menores = 0

for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento: '))

    idade = 2026 - ano

    if idade >= 18:
        maiores += 1

    else:
        menores += 1

print(f'Existem {maiores} maiores de idade e {menores} menores de idade')