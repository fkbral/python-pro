def maxmin(colecao):
    maior = max(colecao)
    menor = min(colecao)
    return maior, menor


numeros = [3, 1, 4, 1, 5, 9, 2]

resposta = maxmin(numeros)
print(resposta)
print(type(resposta))  # mostra o tipo da variável resposta
