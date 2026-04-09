# while X: laço de repetição que acontecerá enquanto uma condição for verdadeira

valor = int(input("Digite um valor: "))

i = 0;

while i < 10:
    valor = valor + 1
    print("O valor atual é:", valor, "e o valor de i é: ", i)
    i = i + 1

print("\nO valor final é: ", valor)