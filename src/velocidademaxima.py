# Escreva um programa que aplique uma multa caso a velocidade seja acima do limite de 80 km/h permitido:
# Até 10km/h por hora acima: multa leve
# Entre 11km/h e 20km/h: multa grave
# Acima de 20km/h: multa gravíssima
# O programa também deve verificar se a CHN está válida. Caso não esteja, deve aplicar multa gravíssima.

cnh = input("Digite se a CNH é válida(S/N): ")
velocidade = int(input("Digite a velocidade do veículo: "))

if cnh.upper() == "S": 
    print("CNH válida.")
else:
    print("CNH inválida! Multa gravíssima aplicada.")
    
if velocidade <= 80:
    print("Velocidade dentro do limite permitido.")
elif velocidade <= 90:
    print("Velocidade acima do limite permitido! Multa LEVE aplicada. Velocidade: ", velocidade, "km/h.")
elif velocidade <= 100:
    print("Velocidade acima do limite permitido! Multa GRAVE aplicada. Velocidade: ", velocidade, "km/h.")
else:
    print("Velocidade acima do limite permitido! Multa GRAVÍSSIMA aplicada. Velocidade: ", velocidade, "km/h.") 