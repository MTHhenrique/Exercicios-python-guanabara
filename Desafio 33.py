# Faça um programa que leia tres numeros e mostre qual e o maior e o menor

primeiro = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))
terceiro = int(input('Digite o terceiro número: '))

# Teste do número maior
if(primeiro >= segundo and primeiro >= terceiro):
    print(f'O número {primeiro} é o maior')

elif(segundo >= primeiro and segundo >= terceiro):
    print(f'O número {segundo} é o maior')

else:
    print(f'O número {terceiro} é o maior')

# Teste do número menor
if(primeiro <= segundo and primeiro <= terceiro):
    print(f'O número {primeiro} é o menor')

elif(segundo <= primeiro and segundo <= terceiro):
    print(f'O número {segundo} é o menor')

else:
    print(f'O número {terceiro} é o menor')