# Maior valor

valor01 = int(input("Digite o primeiro valor: "))
valor02 = int(input("Digite o segundo valor: "))

if valor01 > valor02: 
    print("O maior valor é o valor01:", valor01)
elif valor02 > valor01:
    print("O maior valor é o valor02:", valor02)
else:
    print("Os valores são iguais:", valor01)