numero_de_provas = 4
contador = 0
soma = 0

while contador < numero_de_provas:
    numero = int(input('Entre com um número: '))
    soma = soma + numero
    contador = contador + 1

media = soma/4

print(media)
