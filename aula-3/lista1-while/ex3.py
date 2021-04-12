# Peça ao usuário para digitar um número N e
# some todos os números de 1 a N utilizando o laço de repetição while.

ultimo = int(input('Entre com um número: '))
atual = 1
soma = 0

while atual <= ultimo:
    soma = soma + atual
    atual = atual + 1
print(soma)
