# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar

nome = input('Olá, qual seu nome? ')
reais = float(input('Quantos reais você tem na sua carteira? '))

dolar = float(5.19)

resultado = reais / dolar

print('{}, com os {} reais que você tem, você consegue comprar {} doláres'.format(nome, reais, resultado))
