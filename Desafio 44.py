# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto      à vista no cartão: 5% de desconto      em até 2x no cartão: preço formal       3x ou mais no cartão: 20% de juros

produto = float(input('Qual é o valor do produto? '))
print('\nEssas são nossas formas pagamento:\n1) À vista dinheiro/cheque: 10% de desconto\n2) À vista no cartão: 5% de desconto\n3) Em até 2x no cartão: preço formal\n4) 3x ou mais no cartão: 20% de juros')
pagamento = int(input('Digite o número da forma de pagamento que deseja: '))

if pagamento == 1:
    porcentagem = produto * 10 /100
    final = produto - porcentagem
    print(f'Você ganhou 10% de desconto, o novo valor do produto é R${final}')

elif pagamento == 2:
    porcentagem = produto * 5 /100
    final = produto - porcentagem
    print(f'Você ganhou 5% de desconto, o novo valor do produto é R${final}')

elif pagamento == 3:
    print(f'Você não ganhou desconto, o valor do produto continua igual R${produto}')
    parcela = produto /2
    print(f'O valor da sua parcela ficará em R${parcela}')

elif pagamento == 4:
    porcentagem = produto * 20 /100
    final = produto + porcentagem
    print(f'Você terá que pagar 20% de juros, o novo valor do produto é R${final}')

    vezes = int(input('Em quantas vezes deseja dividir o valor? (Temos até 4 vezes) '))
    if vezes == 1 or vezes == 2:
        print('Você está na opção de pagamento errada, volte para o inicio e leia com atenção!')

    elif vezes == 3:
        parcela = final /3
        print(f'O valor da sua parcela ficará em R${parcela}')

    elif vezes == 4:
        parcela = final /4
        print(f'O valor da sua parcela ficará em R${parcela}')

    else: 
        print('você digitou o número errado, tente novamente!!')

else:
    print('você digitou o número errado, tente novamente!!')