def somaDois(numero1, numero2):
    return numero1 + numero2


def somaLista(numeros):
    total = 0
    for numero in numeros:
        total = total + numero
    return total


def soma(*numeros):
    total = 0
    for numero in numeros:
        total = total + numero
    return total


print(somaDois(10, 5))
print(somaLista([10, 5, 6]))
print(soma(10, 5, 6))
