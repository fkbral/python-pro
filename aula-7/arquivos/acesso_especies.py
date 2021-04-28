import csv

planilha = open('aula-7/arquivos/especies.csv', 'r')
leitor = csv.reader(planilha, delimiter=';', lineterminator='\n')
tabela = []

for linha in leitor:
    tabela.append(linha)

print(tabela[0])
print(tabela[1])
