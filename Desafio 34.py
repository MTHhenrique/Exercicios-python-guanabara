# Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
# Para salarios superiores a R$1.250,00 calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Qual é o salário do funcionário? '))

if (1250 < salario):
    aumento = salario * 10 /100
    novo = salario + aumento

else: 
    aumento = salario * 15 /100
    novo = salario + aumento

print(f'O salário do funcionário teve um aumento de R${aumento:.2f}')
print(f'O novo salário do funcionário é R${novo:.2f}')