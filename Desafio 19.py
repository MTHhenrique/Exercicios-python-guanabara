# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido

import random
a1 = input('Qual é o nome do primeiro aluno? ')
a2 = input('Qual é o nome do segundo aluno? ')
a3 = input('Qual é o nome do terceiro aluno? ')
a4 = input('Qual é o nome do quarto aluno? ')
escolhido = random.choice((a1, a2, a3, a4))

print('O aluno sorteado foi: ', escolhido)