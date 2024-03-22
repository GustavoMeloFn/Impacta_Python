# ex 9) Crie um código em Python que leia um número inteiro qualquer
# e mostre na tela a sua tabuada.
number = int(input('Digite um número: '))
Tabuada = [1, 2 , 3, 4, 5, 6, 7, 8, 9, 10]
for valores in Tabuada:
  resultado = valores * number
  print(f'{number} x {valores} = {resultado}')