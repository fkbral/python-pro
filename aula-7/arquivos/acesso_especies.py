import csv

planilha = open('aula-7/arquivos/especies.csv', 'r', encoding="utf-8")
leitor = csv.reader(planilha, delimiter=';', lineterminator='\n')
tabela = []

for linha in leitor:
    tabela.append(linha)

print(tabela[0])
print(tabela[1])

planilha.close()
