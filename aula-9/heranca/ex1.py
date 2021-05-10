class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.permissoes = []

    def listaPermissoes(self):
        if len(self.permissoes) == 0:
            print('A pessoa não tem permissões')


class Aluno(Pessoa):
    def __init__(self, nome, idade, altura, indice_academico, presenca):
        super().__init__(nome, idade, altura)
        self.indice_academico = indice_academico
        self.presenca = presenca


class Professor(Pessoa):
    def __init__(self, nome, idade, altura):
        super().__init__(nome, idade, altura)
        self.permissoes.append('corrige prova')
        self.permissoes.append('dá presença')

    def listaPermissoes(self):
        permissoes = ' e '.join(self.permissoes)
        print(f'As permissões de um professor são: {permissoes}')


class ProfessorSubstituto(Professor):
    def __init__(self, nome, idade, altura):
        super().__init__(nome, idade, altura)


cleber = Pessoa('Cleber', 33, 1.55)

regina = Aluno('Regina', 24, 1.7, 840, 0.8)

felipe = Professor('Felipe', 29, 1.8)

bruno = ProfessorSubstituto('Bruno', 22, 1.8)

print(cleber.idade)
print(regina.idade)
print(regina.indice_academico)
regina.listaPermissoes()
felipe.listaPermissoes()
bruno.listaPermissoes()

print("="*50)

print(isinstance(regina, Pessoa))
print(isinstance(regina, Aluno))
print(isinstance(regina, Professor))

print("="*50)

print(isinstance(cleber, Pessoa))
print(isinstance(cleber, Aluno))

print("="*50)

print(isinstance(bruno, Pessoa))
print(isinstance(bruno, Aluno))
print(isinstance(bruno, Professor))
print(isinstance(bruno, ProfessorSubstituto))
