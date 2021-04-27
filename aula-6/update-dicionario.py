jogadores = {
    "123.456.789-01": {
        "nome": "Cleber",
        "idade": 20,
        "altura": 1.8,
        "esporte": "basquete",
    },
    "123.456.789-02": {
        "nome": "Michael",
        "idade": 25,
        "altura": 1.85,
        "esporte": "basquete",
    },
    # "123.456.789-03": {
    #     "nome": "Jonas",
    #     "idade": 28,
    #     "altura": 1.9,
    #     "esporte": "basquete",
    # },
    # "time": "Chicago Bulls"
}

# O método update seria o equivalente em dicionários do nosso append de listas
jogadores.update({
    "123.456.789-03": {
        "nome": "Jonas",
        "idade": 28,
        "altura": 1.9,
        "esporte": "basquete",
    },
    "123.456.789-04": {
        "nome": "Mary",
        "idade": 22,
        "altura": 1.82,
        "esporte": "basquete",
    },
})

# Poderia ser feito desta forma também:

# jogadores["123.456.789-03"]: {
#     "nome": "Jonas",
#     "idade": 28,
#     "altura": 1.9,
#     "esporte": "basquete",
# }
# jogadores["123.456.789-04"]: {
#     "nome": "Mary",
#     "idade": 22,
#     "altura": 1.82,
#     "esporte": "basquete",
# }

# Como adicionar novas chaves/valor a um dicionário:

# Método 1
jogadores.update({
    "time": "Chicago Bulls"
})

# Método 2
jogadores["time"] = "Chicago Bulls"

# print(jogadores)
# print(jogadores["123.456.789-01"])
print(jogadores)
