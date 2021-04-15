lista = [10, 9, 9, 10]
lista2 = [7, 6, 8, 10]


def media(numeros):
    soma = 0
    for numero in numeros:
        soma = soma + numero
    media_numeros = soma/len(numeros)

    return media_numeros


media1 = media(lista)
media2 = media(lista2)

print(media1)
print(media2)
