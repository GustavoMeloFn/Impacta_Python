# ex 10) Crie um código em Python que leia quanto dinheiro uma pessoa
# possui e mostre quantos dólares ela poderá comprar.

valorInReais = float(input('Informe a quantidade de valores em reais que possui:'))
conversao = valorInReais / 4.95

print(f'Você consegue comprar esse valor ${conversao:.2f} em dolares')