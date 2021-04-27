tupla = (1, 2, 3, 4, 5)

print(tupla)

for elemento in tupla:
    print(elemento)

# Nossa tupla não tem acesso ao métodos para alterar
# append, pop, remove
# como tínhamos com listas
tupla.append(6)

print(tupla)
