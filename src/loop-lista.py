# loop de X em Y: laço de repetição que irá iterar X vezes em uma coleção de Y

valores = [800, 997, 1200, 497, 1500, 300, 450.59, 600]
soma = 0

for valor in valores:
    print("O valor atual é:", valor)
    soma = soma + valor
    
print("\nA soma dos valores é: ", soma)
print("\n")
nomes = ["Joao", "Maria", "Pedro", "Ana", "Lucas"]

for nome in nomes:
    print("O nome atual é:", nome)
    
print("\nA quantidade de nomes na lista é: ", len(nomes))