# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

genero = input('Qual seu gênero? [F/M] ')

while not genero == 'M' and not genero == 'F':
        genero = input('Escreva novamente: ')

    
print('Tudo certo')