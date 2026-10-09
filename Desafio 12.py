# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

atual = float(input('Qual é o valor atual do produto?'))

desconto = atual * 5 / 100
novo = atual - desconto

print(f'O novo valor do produto será R${novo:.2f}')