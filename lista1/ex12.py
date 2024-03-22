# 12 Contador de notas

loop = 4
notas = 0
qntdNotas = 0
contagem = 1

while loop >= 0:
  notas = int(input(f'Digite a {contagem}° nota:'))
  notas = notas + notas
  qntdNotas = qntdNotas + 1
  contagem = contagem + 1
  loop = loop - 1

notaFinal = notas / qntdNotas
print(f'Média final = {notaFinal}')