
#Funções
def calcular_soma(value01, value02):
    return value01 + value02

def calcular_media(value01, value02):
    return (value01 + value02) / 2

def media_lista(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

valor01 = int(input("Digite o primeiro valor: "))
valor02 = int(input("Digite o segundo valor: "))
lista = [455, 300, 150, 200, 1002]

resultado = calcular_soma(valor01, valor02)
media = calcular_media(valor01, valor02)
media_lista_resultado = media_lista(lista)
print("A soma dos valores é:", resultado)
print("A média dos valores é:", media)
print("A média da lista é:", media_lista_resultado)