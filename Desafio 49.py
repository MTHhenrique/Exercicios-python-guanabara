# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero = int(input('Digite um número: '))
tabuada = 0

for c in range(0, 11):
    resultado = numero * tabuada
    print('{} x {} = {}'.format(numero, tabuada, resultado))
    tabuada = tabuada + 1