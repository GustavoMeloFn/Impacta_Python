# Ex 22) Escreva um programa que leia a velocidade de um carro.
#        Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#        A multa vai custar R$7,00 por cada Km acima do limite.
#        Se a velocidade for menor que 80 km/h escreva "Você não foi multado"

velocidade = float(input("Escreva a  velocidade registrada: "))
multaKm = 0
valorTotal = 0

if velocidade > 80:
  multaKM = (velocidade - 80) * 7

  print(f"Você foi multado em: R${multaKM:.2f}")

else:
  print("Você não foi multado!")