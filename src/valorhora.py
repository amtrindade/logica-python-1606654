salario_mensal = input("Digite o seu salário mensal: ")
horas_trabalhadas = input("Digite o total de horas trabalhadas: ")

valor_hora = float(salario_mensal) / float(horas_trabalhadas)

print(f"O valor da sua hora de trabalho é: R$ {valor_hora:.2f}")