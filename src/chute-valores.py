# Escreva um programa que gere um número aleatório de 1 a 10 
# permita ao usuário chutar um número até que o valor aleatório seja igual ao chute.
# Ao chutar, caso o valor esteja errado, informar se o valor está abaixo ou acima do chute
# O programa deve permitir que no máximo 3 chutes sejam tentados.

import random

numero_aleatorio = random.randint(1, 10)
acertou = False
tentativas = 1

while (acertou == False) and (tentativas <= 3):
    valor_chute = int(input("Chute um número de 1 a 10: "))
    if valor_chute == numero_aleatorio:
        print("Parabéns! Você acertou o número aleatório: ", numero_aleatorio)
        acertou = True
    elif valor_chute < numero_aleatorio:
        print("O número aleatório é maior do que o chute.")
    else:
        print("O número aleatório é menor do que o chute.")
    tentativas = tentativas + 1

if acertou == False:
    print("Suas tentativas acabaram! Você perdeu!! O número aleatório era: ", numero_aleatorio) 

print("Fim do jogo.")