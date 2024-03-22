# Exercicio 5: Crie um código em Phyton que leia um número real e mostre o dobro, triplo, metade e raiz quadrada
import math
number = float(input('Escreva um número: '))

dobro = number * 2
triplo = number * 3
metade = number / 2

# Função math.sqrt serve como a raiz quadrada:
raizQuadrada = math.sqrt(number)

print(f'O dobro de {number} é: {dobro :.2f}')
print(f'O triplo de {number} é: {triplo }')
print(f'O metade de {number} é: {metade :.2f}')
print(f'A raiz quadrada de {number} é: {raizQuadrada:.2f}')