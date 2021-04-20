precoLitro = 5.234
litros = 29.5
total = precoLitro * litros
print(total)  # resultado: 154.403

precoFinal = 'R$ {:.2f}'.format(total)
print(precoFinal)  # resultado: R$ 154.40
