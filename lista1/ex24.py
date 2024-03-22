# Ex 24) faça um código que pergunte o valor do financiamento, números de parcela
#        taxa de juros e determine o valor do financiamento
#        para isso você vai usar a formula abaixo
# P é a parcela,
# PV = valor do financiamento ou empréstimo
# i = taxa de juros
# n = número de parcelar.

pv = float(input("Valor do financiamento: "))
n = int(input("Número de parcelas? "))
i = float(input("Qual a taxa de juros? "))

p = pv * ((1 + i / 100)**n * i/100) / ((1 + i / 100) ** n-1)

print(f"Valor do financiamento: {p:.2f}")