# Escreva um programa que converta uma temperatura digitada em °C e converta para °F

celsius = float(input('Digite a temperatura em celsius: '))

fahrenheit = (celsius * 9 / 5) + 32

print(f'A temperatura de {celsius:.2f}°C é {fahrenheit:.2f}°F')