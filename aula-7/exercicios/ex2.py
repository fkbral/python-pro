# Para o segundo exercício, você deve criar um programa que realize uma
# cópia do arquivo "alunos.csv". Essa cópia deve ser um arquivo chamado
# "alunos_copia.csv".

# Novamente, aqui você também não precisa utilizar a biblioteca CSV mas se usar,
#  seu código pode ser reutilizado na próxima questão sem muitas modificações.

arquivo_original = open('aula-7/exercicios/alunos.csv', 'r', encoding="utf-8")

conteudo = arquivo_original.read()

arquivo_original.close()

arquivo_copia = open('aula-7/exercicios/alunos_copia.csv',
                     'w', encoding="utf-8")

arquivo_copia.write(conteudo)

arquivo_copia.close()
