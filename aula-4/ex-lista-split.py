nomes = ["Roger", "Ana", "Carla", "Edson"]

# print(nomes[0])
# print(nomes[1])
# print(nomes[2])
# print(nomes[3])

# print(nomes[0:2])  # exibo todos os elementos de 0 a 2 (sem incluir o 2)
# exibo todos os elementos de 0 (por padrão) a 2 (sem incluir o 2)
# print([0:4:2])  # exibe os elementos pares (0, 2, 4 ...)
print(nomes[::-1])  # inverte minha lista

novo_nome = input('Entre com um nome para adicionar na lista: ')
nomes.append(novo_nome)

print(nomes)
