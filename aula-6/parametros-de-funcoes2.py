usuarios = {
    "fulano@outlook.com": {
        "nome": "Fulano",
        "idade": 20,
    },
    "ciclano@outlook.com": {
        "nome": "Ciclano",
        "idade": 22,
    },
}


def criaUsuario(**argumentos):
    print(argumentos["email"])
    for chave, valor in argumentos.items():
        if not argumentos["email"] in usuarios:
            usuarios[argumentos["email"]] = {}

        if(chave != 'email'):
            usuarios[argumentos["email"]][chave] = valor


criaUsuario(nome='João', idade=23, email="joao@email.com")

print(usuarios)
