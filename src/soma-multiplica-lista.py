# Escreva um programa que:
# Some os valores que são pares de uma lista
# Multiplique os valores que são ímpares

valores = [20, 9, 8, 7, 6, 5] 

soma = 0
multiplicacao = 1

for valor in valores:
    if valor % 2 == 0:
        print("O valor atual é:", valor, "e é par")
        soma = soma + valor        
    else:
        print("O valor atual é:", valor, "e é ímpar")
        multiplicacao = multiplicacao * valor

print("\nA soma dos valores pares é: ", soma)
print("\nA multiplicação dos valores ímpares é: ", multiplicacao)
