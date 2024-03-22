# 14 Faça um programa que lê uma nota e atribua o seguinte conceito:
# Valores entre 9 e 10 recebem o conceito A
# Valores entre 7 e 8 recebem o conceito B
# Valores entre 5 e 6 recebem o conceito C
# Valores entre 3 e 5 recebem o conceito D
# Valores entre 1, 2 ou 0 recebem o conceito E

nota = int(input("Me diga uma nota: "))

if nota == 9 and nota == 10:
  print(f"{nota} recebe o conceito A")

elif nota == 7 or nota == 8:
  print(f"{nota} recebe o conceito B")

elif nota == 5 or nota == 6:
  print(f"{nota} recebe o conceito C")

elif nota == 3 or nota == 4:
  print(f"{nota} recebe o conceito D")

elif nota == 2 or nota == 1 or nota == 0:
  print(f"{nota} recebe o valor E")

else:
  print("Valor invalido")
