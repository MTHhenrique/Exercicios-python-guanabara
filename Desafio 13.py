# Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento

salario = float(input('Qual é o salário do funcionário? '))

aumento = salario * 15 /100
salario_novo = salario + aumento

print(f'O novo salário do funcionário será R${salario_novo:.2f}')