pergunta1 = 'Mora perto da vítima?(s/n): '
pergunta2 = 'Já trabalhou com a vítima?(s/n): '
pergunta3 = 'Telefonou para a vítima?(s/n): '
pergunta4 = 'Esteve no local do crime?(s/n): '
pergunta5 = 'Devia para a vítima?(s/n): '

resposta1 = input(pergunta1)
resposta2 = input(pergunta2)
resposta3 = input(pergunta3)
resposta4 = input(pergunta4)
resposta5 = input(pergunta5)

resultado = 0

if(resposta1 == 's'):
    resultado = resultado + 1

if(resposta2 == 's'):
    resultado = resultado + 1

if(resposta3 == 's'):
    resultado = resultado + 1

if(resposta4 == 's'):
    resultado = resultado + 1

if(resposta5 == 's'):
    resultado = resultado + 1

if resultado == 5:
    print('Assassino')
elif resultado == 4 or resultado == 3:
    print('cúmplice')
elif resultado == 2:
    print('suspeito')
else:
    print('liberado')
