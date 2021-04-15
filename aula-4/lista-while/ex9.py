# Desafio! - Calcule a soma de até mil
# termos da série 1 + 1/2 + 1/4 + 1/8 + 1/16 + ...

# Dica: Use três variáveis:

# • um contador, que começa em zero
# • uma variável para a soma de todos os termos, que também começa em zero
# • uma variável para cada termo, que começa em 1
#  e a cada loop é dividida por 2.

# A repetição da soma de mil termos pode ser
#  feita com a função while contador < 1000.

contador = 0
soma = 0
elemento = 1

while contador < 1000:
    soma = soma + elemento
    elemento = elemento/2  # 0.5 (1/2), 0.25 (1/4)
    contador = contador + 1

# soma = 0 + 1 = 1
# soma = 1 +

print(soma)
