salario = float(input("Entre com seu salário: "))
taxa = 0

if salario < 1000:
    taxa = 0.02
elif salario > 1000 and salario < 2000:
    taxa = 0.05
elif salario >= 2000 and salario < 3000:
    taxa = 0.07
elif salario >= 3000 and salario < 4000:
    taxa = 0.12
elif salario >= 4000 and salario < 5000:
    taxa = 0.15
else:
    taxa = 0.27

imposto = salario * taxa

print(
    f'Seu salário é de {salario}, portanto você deverá pagar {imposto} de imposto')
