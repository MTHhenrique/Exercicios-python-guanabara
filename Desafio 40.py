# Crie um programa que leia quatro notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO        Média entre 5.0 e 6.9: RECUPERAÇÃO        Média 7.0 ou superior: APROVADO

n1 = float(input('qual é a primeira nota do aluno? '))
n2 = float(input('qual é a segunda nota do aluno? '))
n3 = float(input('qual é a terceira nota do aluno? '))
n4 = float(input('qual é a quarta nota do aluno? '))

soma = n1 + n2 + n3 + n4
media = soma /4

if (media >= 7):
    print(f'O aluno foi aprovado!! Ele ficou com média {media:.1f}')

elif (media >= 5 and media < 7):
    print(f'O aluno está de recuperação!! Ele ficou com média {media:.1f}')

else:
    print(f'O aluno foi reprovado!! Ele ficou com média {media:.1f}')