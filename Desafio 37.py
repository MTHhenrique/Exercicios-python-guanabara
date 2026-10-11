# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal. 

numero = int(input('Digite um número: '))
conversao = int(input('\nEssas são nossas bases de conversão:\n1) Binário\n2) Octal\n3) Hexadecimal\nDigite o número de qual deseja: '))

if (conversao == 1):
    binario = bin(numero)[2:]
    print(f'O número {numero} em binário é {binario}')

elif (conversao == 2):
    octal = oct(numero)[2:]
    print(f'O número {numero} em octal é {octal}')

elif (conversao == 3):
    hexadecimal = hex(numero)[2:]
    print(f'O número {numero} em hexadecimal é {hexadecimal}')

else:
    print('Sinto muito... Você provavelmente digitou o número errado, ou de uma base de conversão que ainda não temos em nosso sistema... \nSe sinta a vontade para tentar novamente :)')