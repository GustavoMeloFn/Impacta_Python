# ex 11) Crie um código em Python que leia a largura e a altura de uma
# parede em metros, calcule a sua área e a quantidade de tinta necessária
# para pintá-la, sabendo que cada litro de tinta pinta uma área de
# 2 metros quadrados.
altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

area = altura * largura
tinta = area / 2

print(f'Quantidade de tinta necessária: {tinta:.0f} litros')