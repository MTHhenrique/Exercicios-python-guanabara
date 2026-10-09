# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre a mensagem dizendo que ele foi multado.
# A multa vai custar R$7.0 por cada km acima do limite

velocidade = int(input('Em que velocidade o carro estava? '))

if (velocidade > 80):
    acima = velocidade - 80
    valor = acima * 7
    print(f'Você foi multado! Você estava {acima}km acima do limite e terá que pagar o valor de R${valor}')

else: 
    print('Você estava na velocidade correta! Siga com segurança e tenha um bom dia!!')