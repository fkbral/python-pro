# Faça um programa que recebe um número inteiro do
# usuário e imprime na tela a quantidade de divisores
# desse número e quais são eles.

divisor = 1
numero = int(input('Entre com um número: '))

while divisor <= numero/2:
    if numero % divisor == 0:
        print(divisor)
    divisor = divisor + 1
