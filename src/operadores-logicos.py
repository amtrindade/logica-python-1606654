### Operadores lógicos em Python
# and
# or
# not

# Operadores de comparação
# == igual a
# > maior que

idade = 26

if idade == 25:
    print("Você tem 25 anos.")
elif idade > 25:
    print("Você tem mais de 25 anos.")
else:
    print("Você tem menos de 25 anos.")    
 
# != diferente de   
if idade != 25:
    print("Você não tem 25 anos.")
    print(f"Você tem {idade} anos.")
else:
    print("Você tem 25 anos.")
    print("Você é jovem ainda.")    

# >= maior ou igual a
# <= menor ou igual a

altura = 1.79

if (altura >= 1.80):
    print("Você é alto.")
else:
    print("Você é baixo.")
    
# Operadores lógicos
# not

# and
valor01 = 6
valor02 = 30

if (valor01 > 5) and (valor02 < 30):
    print("As duas condições são verdadeiras.")
else:
    print("Pelo menos uma das condições é falsa.")  

# or
if (valor01 > 5) or (valor02 < 30):
    print("Pelo menos uma das condições é verdadeira.")
else:
    print("As duas condições são falsas.")
  
# not
if not (valor01 > 5):  
    print("A condição é falsa.")
else:
    print("A condição é verdadeira.")