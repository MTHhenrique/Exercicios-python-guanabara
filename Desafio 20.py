# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

import random

a1 = input('Qual é o nome do primeiro aluno? ')
a2 = input('Qual é o nome do segundo aluno? ')
a3 = input('Qual é o nome do terceiro aluno? ')
a4 = input('Qual é o nome do quarto aluno? ')

alunos = [a1, a2, a3, a4]
random.shuffle(alunos)

print(f'A ordem da apresentação dos alunos é {alunos}')