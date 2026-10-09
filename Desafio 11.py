#faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m²

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))

area = largura * altura
tinta = area / 2

print(f'A área da parede é de {area}m².')
print(f'Você precisará de {tinta} litros de tinta para pintar a parede.')
