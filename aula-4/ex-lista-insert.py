nomes = ["Roger", "Ana", "Carla", "Edson"]

novo_nome = input('Entre com um nome para adicionar na lista: ')
nomes.insert(2, novo_nome)

# diferentemente do método insert, remove dá erro quando o valor não existe
if 'Carla' in nomes:  # estrutura if in nos permite checar existência de valor em uma lista
    nomes.remove('Carla')

print(nomes)
