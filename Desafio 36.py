# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o seu salário? '))
anos = int(input('Pretende pagar a casa por quantos anos? '))

prestacao = casa / (anos * 12)
porcentagem = salario * 30 /100

if (porcentagem >= prestacao):
    print('Parabéns!! Seu empréstimo foi aprovado!!')

else:
    print('Que pena... seu empréstimo foi negado!')