# O que eu tenho à esquerda dos :
# seriam as chaves,
# à direita, valores
# "chave" : valor
jogador = {
    "nome": "João",
    "idade": 19,
    "time": "São Paulo",
    "altura": 1.88,
    "ativo": True,
    "colegas": ["Fulano", "Ciclano"],
    "dependentes": [
        {
            "nome": "Maria",
            "idade": 1,
        },
        {
            "nome": "Zeca",
            "idade": 2,
            "primeiroFilho": True
        },
    ],
}

print(jogador)
print(jogador["nome"])
print(jogador["dependentes"])
print(jogador["dependentes"][0])
print(jogador["dependentes"][1])
