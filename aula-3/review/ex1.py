idade = int(input('Digite a idade: '))

if idade < 0 or idade > 150:
    print('Erro')
elif idade >= 18:
    print('Você já pode tirar carteira de motorista')
