# ex 7) Crie um código em Python que leia o nome do aluno e duas
#       notas com números reais. Calcule a média desse aluno e de
#       a resposta com 1 casa decimal.

nomeAluno = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota:'))

media = (nota1 + nota2) / 2

print(f'A média final do aluno {nomeAluno} é de: {media}')