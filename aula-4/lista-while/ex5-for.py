numero = int(input('Entre com um número: '))
divisores = []

for divisor in range(1, numero+1):
    if numero % divisor == 0:
        divisores.append(divisor)
    divisor = divisor + 1

print(divisores)
