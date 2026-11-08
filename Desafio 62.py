# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos. 

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))

termo = primeiro
contador = 0
total = 10

while contador < total:
    print(termo)
    termo += razao
    contador += 1

mais = int(input('Quantos termos você quer mostrar a mais? '))

while mais != 0:
    total += mais
    while contador < total:
        print(termo)
        termo += razao
        contador += 1
    mais = int(input('Quantos termos você quer mostrar a mais? '))

print('Progressão finalizada!')