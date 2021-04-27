# 1. Listar todos os usuários do sistema
# 2. Incluir novos usuários no sistema
# 3. Buscar por um usuário no sistema
# 4. Sair do programa

lista_usuarios = []
opcao = -1


def mostraMenu():
    print("="*50)
    print("1. Listar todos os usuários do sistema")
    print("2. Incluir novos usuários no sistema")
    print("3. Buscar por um usuário no sistema")
    print("4. Sair do programa")
    # print("\n"*4)


def listaUsuarios(usuarios):
    print(usuarios)


def executaOperacao(operacao, usuarios):
    if operacao == 1:
        return listaUsuarios(usuarios)
    if operacao == 2:
        return adicionaUsuario(usuarios)
    if operacao == 3:
        email = input("Entre com o email do usuário procurado: ")
        return buscaPorUsuario(usuarios, email)


def adicionaUsuario(usuarios):
    name = input("Entre com o nome do usuário: ")
    email = input("Entre com o email do usuário: ")
    age = int(input("Entre com a idade do usuário: "))
    usuarios.append(
        {
            "nome": name,
            "idade":  age,
            "email": email,
        }
    )


def buscaPorUsuario(usuarios, email):
    for usuario in usuarios:
        if usuario["email"] == email:
            return print(f'O usuário foi encontrado e tem os dados: {usuario}')
    return print('O usuário não existe no sistema')


while opcao != 4:
    mostraMenu()
    opcao = int(input("Entre com uma opção:"))
    executaOperacao(opcao, lista_usuarios)
