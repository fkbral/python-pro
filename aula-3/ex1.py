nome = input('Entre com seu nome: ')

erros = 0

while nome != 'Caroline' and nome != 'Enrico':
    erros = erros + 1
    print('Ops, nome inválido')
    nome = input('Entre com seu nome: ')

print('Seu nome é', nome)
print('Você teve', erros, 'erros')
