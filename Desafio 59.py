# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar    [ 2 ] multiplicar    [ 3 ] maior    [ 4 ] novos números   [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso. 

print('Olá, seja bem vindo(a) ao menu')
print('\n')

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
print('\n')

print('Temos as seguintes opções: \n1] Somar \n2] Multiplicar \n3] Maior \n4] Novos números \n5] Sair do programa')
escolhido = int(input('Qual opção deseja? '))
print('\n')

while escolhido <= 4:
    if escolhido == 1:
        soma = n1 + n2
        print(f'{n1} + {n2} = {soma}')

        escolhido = int(input('Deseja mais alguma coisa? '))
        print('\n')

    elif escolhido == 2:
        soma = n1 * n2
        print(f'{n1} x {n2} = {soma}')

        escolhido = int(input('Deseja mais alguma coisa? '))
        print('\n')

    elif escolhido == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')

        elif n1 < n2:
            print(f'{n2} é maior que {n1}')

        else:
            print(f'{n1} e {n2} são iguais')

        escolhido = int(input('Deseja mais alguma coisa? '))
        print('\n')

    elif escolhido == 4:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))

        escolhido = int(input('O que deseja fazer com esses números? '))
        print('\n')

    else:
        print('Você provavelmente digitou errado... Tente novamente')
        print('Temos as seguintes opções: \n1] Somar \n2] Multiplicar \n3] Maior \n4] Novos números \n5] Sair do programa')
        escolhido = int(input('Qual opção deseja? '))

print('Fim do programa!')