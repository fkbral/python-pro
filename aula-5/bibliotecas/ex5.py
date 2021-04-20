import random

numeros_sorteados = []
numeros_apostados = []
numeros_totais = 6
acertos = 0


def premia(acertos):
    if acertos == numeros_totais:
        return('Parabéns você ganhou a melhor premiação')
    if 5 >= acertos >= 3:
        return('Parabéns você ganhou a segunda melhor premiação')
    return('Infelizmente você perdeu... tente novamente numa próxima vez')


for contador in range(numeros_totais):
    sorteio = random.randrange(1, 61)
    while sorteio in numeros_sorteados:
        sorteio = random.randrange(0, 61)
    numeros_sorteados.append(sorteio)

print(numeros_sorteados)

for contador in range(numeros_totais):
    aposta = int(input(f'Entre com o número {contador + 1}:'))
    while aposta in numeros_apostados:
        print('Número já escolhido! Por favor entre com um novo número')
        aposta = int(input(f'Entre com o número {contador + 1}:'))
    numeros_apostados.append(aposta)

for aposta in numeros_sorteados:
    if aposta in numeros_apostados:
        acertos = acertos + 1

print("Você teve acertos:", acertos)
print(premia(acertos))
