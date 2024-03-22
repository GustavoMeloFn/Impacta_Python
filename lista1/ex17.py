# ex 17) Escreva um programa que converta uma temperatura digitando
#        em graus Celsius e converta para graus Fahrenheit.

temp = int(input("Digite a temperatura atual em °C: "))

F = (temp * 1.8) + 32

print(f"Temperatura convertida para Fahrenheit: °F{F}")