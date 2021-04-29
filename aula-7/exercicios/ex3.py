# Finalmente chegamos ao último exercício dessa sequência relacionada à
#  manipulação de arquivos.

# Neste exercício você deve criar um novo arquivo chamado "alunos_media.csv".
# Esse novo arquivo é uma cópia de "alunos.csv" porém com uma coluna a mais
# chamada "Média" que vai abrigar os valores das médias das provas de cada
# aluno da lista.

# Se você utilizou a biblioteca CSV para realizar os dois primeiros exercícios,
#  muito será reaproveitado aqui. A biblioteca CSV permite a interpretação de
# cada linha como listas, que são fáceis de manipular.

import csv

arquivo_original = open('aula-7/exercicios/alunos.csv', 'r')
arquivo_final = open('aula-7/exercicios/alunos_media.csv', 'w')
leitor = csv.reader(arquivo_original, delimiter=",", lineterminator="\n")
escritor = csv.writer(arquivo_final, delimiter=",", lineterminator="\n")

tabela = []

for line in leitor:
    tabela.append(line)

arquivo_original.close()

header = tabela.pop(0)
header.append("Media")

for indice in range(len(tabela)):
    media = (float(tabela[indice][3]) + float(tabela[indice][4]) +
             float(tabela[indice][5]) + float(tabela[indice][6]))/4
    tabela[indice].append(media)

tabela.insert(0, header)

escritor.writerows(tabela)
arquivo_final.close()
