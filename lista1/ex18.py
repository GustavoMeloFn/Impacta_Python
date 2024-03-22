# ex 18) Escreva um programa que pergunte a quantidade de Km
#        percorridos por um carro alugado e a quantidade de dias
#        pelos quais ele foi alugado. Calcule o preço a pagar,
#        sabendo que o carro custa R$60 por dia e R$0,15 por Km
#        rodado.

print("Carro alugado")
qntdKms = float(input("Quantos Kms foram percorridos? "))
qntdDias = float(input("Quantos dias foram gastos? "))

precoKm = qntdKms * 0.15
precoDias = qntdDias * 60

precoTotal = precoDias + precoKm

print(f"Valor total do carro alugado: {precoTotal}")