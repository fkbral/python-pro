numeros = [1200, 300, 2, -111, 44, 0, 10, 300]
# for indice in [0,1,2,3,4,5]
nomes = ['zorro', 'mARIA alves', 'Alex sousa', 'bruno', 'Zulmira', 'alexandre']
nomes_corrigidos = []
for indice in range(len(nomes)):
    nomes[indice] = nomes[indice].capitalize()

for nome in nomes:
    nome = nome.capitalize()
    nomes_corrigidos.append(nome)

numeros.sort()
nomes.sort()
# Inverte a lista
# funciona da mesma forma que nomes[::-1]
nomes_corrigidos.sort()

print(numeros)
print(nomes)
print(nomes_corrigidos)
