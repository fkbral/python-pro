import csv

tabela_especies = [
    ["especie", "população", "região típica"],
    ["canguru", 200000, "Austrália"],
    ["castor", 300000, "América do Norte"],
]

planilha = open("especies.csv", "w", encoding="utf-8")

escritor = csv.writer(planilha, delimiter=";", lineterminator="\n")

escritor.writerows(tabela_especies)
