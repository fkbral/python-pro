idade = int(input('Digite a idade: '))

while idade < 0 or idade > 150:
    print('Erro! Idade deve estar entre 0 e 150!')
    idade = int(input('Digite a idade: '))

print('Obrigado!')

# Condição de saída de loops:
# Negar a condição para entrar em nosso loop

# Condição de entrada: idade < 0 or idade > 150
# Para ter minha condição de saída aplico o not na condição de entrada

# not(idade < 0 or idade > 150)
# idade >= 0 and idade <= 150
