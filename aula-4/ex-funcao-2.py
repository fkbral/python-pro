def sauda(horas, nome='Fulano'):
    if horas < 12:
        print(f'Bom dia, {nome}!')
    elif horas >= 12 and horas < 18:
        print(f'Boa tarde, {nome}!')
    elif horas <= 23:
        print(f'Boa noite, {nome}!')


def saudaComRetorno(horas):
    if horas < 12:
        return 'Bom dia!'
    print('não é dia')
    if horas >= 12 and horas < 18:
        return 'Boa tarde!'
    print('não é tarde')
    if horas <= 23:
        return 'Boa noite!'


# saudacao = saudaComRetorno(15)
# print(saudacao)

sauda(20)
sauda(14, 'Cláudia')
