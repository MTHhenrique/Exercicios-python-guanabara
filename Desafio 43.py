# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso       Entre 18,5 e 25: Peso Ideal        – 25 até 30: Sobrepeso        30 até 40: Obesidade          Acima de 40: Obesidade Mórbida 

peso = float(input('Qual é seu peso? '))
altura = float(input('Qual é sua altura? '))

imc = peso / (altura ** 2)

if (imc < 18.5):
    print(f'Seu imc é {imc:.2f}, você está abaixo do peso!')

elif (imc < 25):
    print(f'Seu imc é {imc:.2f}, você está com o peso ideal, continue assim!!')

elif (imc <= 30):
    print(f'Seu imc é {imc:.2f}, você está com sobrepeso!')

elif (imc <= 40):
    print(f'Seu imc é {imc:.2f}, você está com obesidade, se cuide!!')

else:
    print(f'Seu imc é {imc:.2f}, você esta com obesidade mórbida, é extremamente importante que você se cuide!!')