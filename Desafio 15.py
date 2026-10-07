# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 reais por dia e R$0.15 por Km rodado

nome = input('Olá, qual seu nome? ')
dias = int(input('Você ficou por quantos dias com o carro? '))
km = float(input('Quantos km foram percorridos? '))

dias = dias * 60
km = km * 0.15
total = km + dias

print('{}, o valor que você devera pagar é de {}'.format(nome, total))