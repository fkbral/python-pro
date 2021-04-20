# Quero fazer um programa que torne a primeira letra de cada nome
# do meu usuário em maiscúla

# frutas = 'morango; uva; banana; pêra'
# lista_com_frutas = frutas.split('; ')
# print(lista_com_frutas)

nome = 'fulano siLVa DE SouSA'
nome_correto = ''
# Método split está disponível em strings e fornece uma lista com o
# separador fornecido
# string.split(separador)
lista_com_nomes = nome.split(' ')

print(lista_com_nomes)

for nome in lista_com_nomes:
    # print('Valor atual do nome', nome_correto)
    # print('Nome retirado da lista', nome)
    if nome.lower() == 'de':
        nome_correto = nome_correto + ' ' + nome.lower()
    else:
        nome_correto = nome_correto + ' ' + nome.capitalize()

print(nome_correto.strip())
