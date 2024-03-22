# Exercício 6: Crie um programa em Phyton que leia o nome do aluno e duas notas com numero reais.
# Cálcule a média desse aluno e dê a resposta com uma casa decimal

name = input('Nome do aluno: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

notaFinal = (nota1 + nota2) / 2

print(f'Nota final do aluno {name}: {notaFinal:.3}')

if notaFinal > 7:
  print('\033[33m aluno aprovado')
else:
  print('Aluno reprovado')