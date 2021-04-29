arquivo = open('aula-7/arquivos/ola.txt', 'a')
arquivo.write('Olá mundo!\n')  # escreve "Olá mundo" no arquivo
arquivo.close()  # fecha e salva o arquivo

arquivo = open('aula-7/arquivos/ola.txt', 'r')
conteudo = arquivo.read()
print(conteudo)
arquivo.close()
