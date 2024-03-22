# Ex 23) Crie um programa que leia um número inteiro e mostre na tela
 #        se ele é PAR ou ÍMPAR.

valor = int(input("Insira o valor"))

final = valor % 2

if final == 0:
  print("O valor é Par")

else:
  print("O valor é ímpar")