### ========== Variáveis do tipo string (str) texto ==========

nome = "Joao"
sobrenome = "Silva"

print("\nVariáveis do tipo string (str) texto:")
print(f"Seu nome completo é: {nome} {sobrenome}")
print("O tipo da variável nome é: " + str(type(nome))) 
print("O tipo da variável sobrenome é: " + str(type(sobrenome))) # Verificando o tipo da variável


### ========== Variáveis do tipo integer (int) ==========
print("\nVariáveis do tipo integer (int):")

idade_marido = 30
idade_esposa = 28

idade_casal = idade_marido + idade_esposa

print(f"A idade do casal é: {idade_casal}")
print("O tipo da variável idade_marido é: " + str(type(idade_marido))) 
print("O tipo da variável idade_esposa é: " + str(type(idade_esposa))) 
print("O tipo da variável idade_casal é: " + str(type(idade_casal)))

### ========== Variáveis do tipo float (float) números decimais ==========
print("\nVariáveis do tipo float (float) números decimais:")

altura = 1.80
peso = 97.5

imc = peso / (altura * altura)

print(f"Seu IMC é: {imc:.3f}")
print("O tipo da variável altura é: " + str(type(altura))) 
print("O tipo da variável peso é: " + str(type(peso))) 
print("O tipo da variável imc é: " + str(type(imc)))