# loop de X a Y: laço de repetição que irá iterar de X a Y

valor = int(input("Digite um valor: "))

# O range é uma função que gera uma sequência de números, começando do 0 por padrão,
# e incrementando de 1 (por padrão), e parando antes de um número especificado.
for i in range(1, 11):
    valor = valor + 1
    print("O valor atual é:", valor, "e o valor de i é: ", i)
    
print("\nO valor final é: ", valor)   