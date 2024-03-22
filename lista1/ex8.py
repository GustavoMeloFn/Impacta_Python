# ex 8) Crie um código em Python que de leia um valor em metros e
# exiba o valor em centímetros e milímetros. No mesmo programa entre
# com uma informação em km e o programa deve exibir a distância em
# metros e centímetros.

metro = float(input(' Digite o valor em metro: '))
centimetro = metro * 100
milimetro = metro * 1000

print(f' Valor em metro digitado: {metro} \n Valor em centimetro: {centimetro:.2f} \n Valor em milimetro: {milimetro:.2f}')

print('------------------------------------------------------------------')

km = float(input(' Digite um valor em km: '))
centimetro2 = km * 100000
metro2 = km * 1000

print(f' Valor em Km digitado: {km} \n Valor em centimetro: {centimetro2:.2f} \n Valor em metro: {metro2:.2f}')