# ex 20) Escreva um código que resolva a uma equação do 2° grau usando a formula de Bhaskara
#        lembre-se que se delta < 0 não existe raiz no conjunto dos números reais
#        Se desta < 0 escreva "A equação não tem solução pois delta = {delta} < 0"
#        Caso contrario resolva a equação e escreva as duas raizes
import numpy as np

a = int(input("valor de A: "))
b = int(input("valor de B: "))
c = int(input("valor de C: "))

delta = b**2 - 4 * a * c

# Quando delta der um valor negativo, quer dizer que não tem uma raíz:
if delta < 0:
  print("A equação não tem raiz")

# Caso contrário, fazemos os cálculos:
else:
  x1 = (-b + np.sqrt(delta)) / (2*a)
  x2 = (-b - np.sqrt(delta)) / (2*a)
  print(f"As raizes da equação são {x1} e {x2}")