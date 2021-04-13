# Neste exemplo len(lista) retorna 4, que é o tamanho de nossa lista
# range(len(lista)), que equivale a range(4) vai nos gerar uma lista
# com os elementos [0, 1, 2, 3]

# Primeira forma de iterar uma lista:

lista = ['Felipe', 20, 'let\'s code', 40]

for elemento in lista:
    eh_string = str == type(elemento)
    # print('O elemento', elemento, 'é do tipo', type(elemento))
    print(f'O elemento, {elemento} é do tipo {type(elemento)}')
    print(eh_string)
