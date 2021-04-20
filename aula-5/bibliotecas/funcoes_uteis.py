nome = "Maria"


def soma(numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero  # mesma coisa que resultado = resultado + numero
    return resultado


def media(numeros):
    somatorio = soma(numeros)
    media = somatorio/len(numeros)
    return media
