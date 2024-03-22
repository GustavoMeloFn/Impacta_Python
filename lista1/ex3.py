# Exercicio 3: Crie um código em Phyton que leia dois número e efetue a soma, subtração, multiplicação, divisão e o número 1 elevado ao número 2
number1 = float(input('Escreva o primeiro número: '))
number2 = float(input('Escreva o segundo número: '))

# Soma:
soma = number1 + number2
print(f'A soma de {number1} + {number2} é igual a: {soma}')

# Subtração
subtracao = number1 - number2
print(f'A subtração de {number1} - {number2} é igual a: {subtracao}')

# Multiplicação
mult = number1 * number1
print(f'A multiplicação de {number1} x {number2} é igual a: {mult}')

# Divisão
div = number1 / number2
print(f'A divisão de {number1} / {number2} é igual a: {div}')

# Primeiro número elevado ao segundo ( .3f após a variável indica quantas casas decimais eu quero que o programa mostre )
elevado = number1 ** number2
print(f'{number1} elevado a {number2} é igual a: {elevado:.3f}')