# Nossas listas sempre começam do índice 0 e
# vão até o índice n - 1, onde n é o número de elementos
# Exemplo:
# numeros = [10, 8, 6, 7]
# Começa no 0 e termina no 3
nomes = ['Felipe', 'Geraldo', 'Jonas', 'Beatriz', 'Maria']
contador = 0

while contador < len(nomes):
    print(nomes[contador])
    contador = contador + 1
