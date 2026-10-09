# Faça um programa que leia um ano qualquer e mostre na tela se ele é bissexto

ano = int(input('Digite algum ano para saber se ele é bissexto: '))
resto = ano % 4
resto2 = ano % 100
resto3 = ano % 400

if (resto == 0 and resto2 > 0 or resto3 == 0):
    print(f'O ano de {ano} é bissexto')

else:
    print(f'O ano de {ano} não é bissexto')