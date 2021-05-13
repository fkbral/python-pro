import requests

# a opção stream = True evita que o Python baixe o arquivo inteiro na memória antes de prosseguir
# ele vai baixando com o programa rodando
resposta = requests.get('https://letscode.com.br/images/logoLcPng.png', stream = True)
arquivo = open('aula-11/logo-letscode.png', 'wb') # cria um arquivo para escrever em binário

# o conteúdo é dividido em blocos - vamos escrever o arquivo pedacinho por pedacinho
for bloco in resposta.raw:
    arquivo.write(bloco) # escreve o binário da requisição

arquivo.close() # salva o arquivo