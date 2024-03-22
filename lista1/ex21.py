# Ex 21)  Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de
#         um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import numpy as np

compCatetoOposto = float(input("Digite o comprimento do cateto oposto: "))
compCatetoAdj = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = np.sqrt(compCatetoOposto**2 + compCatetoAdj**2)

print(f"O valor da hipotenusa é = {hipotenusa :.2f}")