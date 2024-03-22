# 13 Faça um algoritmo que leia o preço de um produto, a taxa de desconto
# e mostre o seu novo valor com o desconto:

preco = float(input('Digite o valor do produto: '))
desc = float(input('Qual a taxa de desconto aplicada: '))
total = (preco * desc) / 100
resultado = preco - total
print(f'Valor total do produto: {resultado}')