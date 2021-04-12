idade = int(input('Entre com sua idade: '))

if idade >= 18:
    tem_CNH = input('Você possui CNH? (digite s para sim ou n para não): ')
    if tem_CNH == 's':
        print('Você pode dirigir')
    else:  # else apenas pode ser utilizado estando relacionado a um if na mesma coluna/nível de identação
        print('Você não pode dirigir')
else:
    print('Você não pode dirigir')
