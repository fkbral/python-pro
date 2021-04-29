# Neste exercício você deve criar um programa que abra o arquivo
# "alunos.csv" e imprima o conteúdo do arquivo linha a linha.

# Note que esse é o primeiro exercício de uma sequência, então o
# seu código pode ser reaproveitado nos exercícios seguintes.
# Dito isso, a recomendação é usar a biblioteca CSV para ler o
# arquivo mesmo que não seja realmente necessário para esse primeiro item.

arquivo = open("aula-7/exercicios/alunos.csv", "r")

linha = "antes de ler arquivo"

while linha:
    linha = arquivo.readline().split('\n')[0]
    if linha:
        print(linha)
