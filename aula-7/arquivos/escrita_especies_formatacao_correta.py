import csv

tabela_especies = [
    ["espécie", "população", "região típica"],
    ["canguru", 200000, "Austrália"],
    ["castor", 300000, "América do Norte"],
]

caminho = "aula-7/arquivos/especies.csv"

planilha = open(caminho, "w", encoding="utf-8")
planilha.write('\uFEFF')
planilha.close()

planilha = open(caminho, "a", encoding="utf-8")

escritor = csv.writer(planilha, delimiter=";", lineterminator="\n")
escritor.writerows(tabela_especies)

planilha.close()
