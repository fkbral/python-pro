nome = input('Entre com seu nome: ')
email = input('Entre com seu email: ')
idade = int(input('Entre com sua idade: '))

dirige_ha = idade - 18

print(dirige_ha)

print(nome, email, idade)

print(nome, ', você poderia dirigir há', dirige_ha, 'anos')

print(f'{nome}, você poderia dirigir há {dirige_ha} anos')
