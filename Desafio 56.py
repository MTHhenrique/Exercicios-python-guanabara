# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

# Alterei um pouco esse pra adicionar diferentes tipos de gênero

velho = 0
soma = 0
mulheres_20 = 0

#Contagem de gêneros
quant_homem = 0
quant_mulher = 0
quant_nb = 0

for c in range(1, 5):

    # Questionário
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    print('Os números referentes a cada gênero:\n1] Feminino / Mulher\n2] Masculino / Homem\n3] Outros / Não binário')
    genero = int(input('Digite o gênero a qual a pessoa se identifica: '))
    print('\n')

    # Calculo de média
    soma += idade
    media = soma / 4

    # if com base nos gêneros
    if genero == 1:
        quant_mulher += 1

        if idade < 20:
            mulheres_20 += 1

    if genero == 2:
        quant_homem += 1

        if velho < idade:
            velho = idade
            nome_velho = nome

    if genero == 3:
        quant_nb += 1

# Saída dos valores
print(f'A média das idades é {media}')

if quant_mulher > 0:
    print(f'Tem {mulheres_20} mulher(es) abaixo dos 20 anos')

if quant_homem > 0:
    print(f'O nome do homem mais velho é {nome_velho}')

if quant_nb > 0:
    print(f'Tem {quant_nb} pessoa(s) não binárias na lista')