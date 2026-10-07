# Desenvolva um programa que leia as notas de um aluno, calcule e mostre sua média

nome = input('Qual é o nome do aluno? ')
n1 = float(input('Qual foi a primeira nota do aluno? '))
n2 = float(input('Qual foi a segunda nota do aluno? '))
n3 = float(input('Qual foi a terceira nota do aluno? '))
n4 = float(input('Qual foi a quarta nota do aluno? '))

soma = n1 + n2 + n3 + n4
media = soma / 4

print('A média das notas do aluno {} foi: {:.2f}'.format(nome, media))