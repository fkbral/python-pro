numero_de_provas = 4
contador = 0
soma = 0
notas_de_provas = []

while contador < numero_de_provas:
    numero = int(input('Entre com um número: '))
    notas_de_provas.append(numero)
    contador = contador + 1

media = sum(notas_de_provas)/4

print('A lista de notas do aluno é', notas_de_provas)
print(media)
