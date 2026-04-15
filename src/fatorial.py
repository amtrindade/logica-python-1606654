# Forma clássica de calcular o fatorial usando um loop
numero = int(input("Digite um número para calcular o fatorial: "))

fatorial = 1

for i in range(1, numero + 1):
    fatorial = fatorial * i
    
print("Final: O fatorial de", numero, "é:", fatorial)

# Outra forma de calcular o fatorial usando recursão
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)  
    
numero = int(input("Digite um número para calcular o fatorial: "))
resultado = fatorial(numero)
print("Recursivo: O fatorial de", numero, "é:", resultado)  