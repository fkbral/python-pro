nome = 'Felipe'
cpf = '123.456.789-01'
rua = 'Rua X'

contrato = 'Eu, {}, portador do CPF {}, residente no endereço {} autorizo o procedimento.'
print(contrato.format(nome, cpf, rua))

print(f'Eu, {nome}, portador do CPF {cpf}, residente no endereço {rua} autorizo o procedimento.')
