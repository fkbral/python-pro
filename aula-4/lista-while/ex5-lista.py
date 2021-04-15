divisor = 1
numero = int(input('Entre com um número: '))
divisores = []

while divisor <= numero:
    if numero % divisor == 0:
        divisores.append(divisor)
    divisor = divisor + 1

print(divisores)
