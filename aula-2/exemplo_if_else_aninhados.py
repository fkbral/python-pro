salario = float(input("Entre com seu salário: "))
imposto = 0

if salario < 1000:
    imposto = salario * 0.02
else:
    if salario > 1000 and salario < 2000:
        imposto = salario * 0.05
    else:
        if salario >= 2000 and salario < 3000:
            imposto = salario * 0.07
        else:
            if salario >= 3000 and salario < 4000:
                imposto = salario * 0.12
            else:
                if salario >= 4000 and salario < 5000:
                    imposto = salario * 0.15
                else:
                    imposto = salario * 0.27

print(
    f'Seu salário é de {salario}, portanto você deverá pagar {imposto} de imposto')
