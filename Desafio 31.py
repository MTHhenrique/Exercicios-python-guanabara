# Desenvolva um programa que pergunte a distancia de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0.50 por km para viagens de ate 200km e R$0.45 para viagens mais longas

distancia = int(input('Qual a distancia da viagem em km? '))

if (distancia <= 200):
    valor = distancia * 0.50

else:
    valor = distancia * 0.45

print(f'O valor da sua viagem de {distancia}km de distancia ficou por R${valor:.2f}')