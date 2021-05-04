class Jogador:
    def __init__(self, nome, idade, altura):
        self.name = nome
        self.age = idade
        self.height = altura

    def imprimeJogador(self):
        print(
            f'O/A jogador(a) se chama {self.name}, possui {self.age} anos de idade e mede {self.height}')

    def __repr__(self):
        return(f'O/A jogador(a) se chama {self.name}, possui {self.age} anos de idade e mede {self.height}')


jogador1 = Jogador('Felipe', 29, '1.78m')
jogadora2 = Jogador('Clara', 22, '1.72m')
print(jogador1.name)
print(jogadora2.name)
print(jogador1)
jogadora2.imprimeJogador()
