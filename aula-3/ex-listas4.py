# Neste exemplo len(lista) retorna 4, que é o tamanho de nossa lista
# range(len(lista)), que equivale a range(4) vai nos gerar uma lista
# com os elementos [0, 1, 2, 3]

# Primeira forma de iterar uma lista:

lista = ['Felipe', 20, 'let\'s code', 40]

for contador in range(len(lista)):
    print(lista[contador])

print('='*50)

# Por debaixo dos panos o python executa este
# primeiro for da seguinte maneira:

for contador in [0, 1, 2, 3]:
    print(lista[contador])

print('='*50)

# Segunda forma de iterar uma lista:

for elemento in lista:
    print(elemento)

print('='*50)

# Por debaixo dos panos o python executa este
# segundo for da seguinte maneira:

for elemento in ['Felipe', 20, 'let\'s code', 40]:
    print(elemento)
