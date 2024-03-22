# ex 19) Escreva um código com o seguinte menu
#        digite 1 para converter a temperatura de graus Celsius para graus Fahrenheit
#        digite 2 para converter a temperatura de graus Fahrenheit para graus Celsius
#        digite 3 para converter a temperatura de graus Celsius para Kelvin
#        digite 4 para converter a temperatura de Kelvin para graus Celsius
#        Se o número digitado for diferente de 1,2,3,4 escrever "Valor inválido"

escolhaUser = int(input("Escolha uma opção: \n 1 para converter a temperatura de graus Celsius para graus Fahrenheit \n 2 para converter a temperatura de graus Fahrenheit para graus Celsius digite \n 3 para converter a temperatura de graus Celsius para Kelvin digite \n 4 para converter a temperatura de Kelvin para graus Celsius \n"))

def conv1():
  temp = int(input("Digite a temperatura atual em °C: "))
  F = (temp * 1.8) + 32
  print(f"Temperatura convertida para Fahrenheit: °F{F}")

def conv2():
  tempF = int(input("Digite a temperatura atual em °F: "))
  C = (tempF * -32) * 9/5
  print(f"Temperatura convertida de Fahrenheit para Celcius: {C}")

if escolhaUser == 1:
  conv1()
elif escolhaUser == 2:
  conv2()

