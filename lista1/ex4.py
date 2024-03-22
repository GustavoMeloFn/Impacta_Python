# Exercicio 4: Crie um código em Phyton que peça ao usuário que digite um número inteiro e escreva o seu antecessor e seu sucessor
choiceNumber = int(input("Escreva um número: "))
sucessor = choiceNumber + 1
antecessor = choiceNumber - 1

print(f' O antecessor do número {choiceNumber} é: {antecessor} \n E o seu sucessor é: {sucessor}')