# Sempre retorna False(falso) a não ser que todos os termos sejam verdadeiros(True)

e_noite = True
estou_desenvolvendo = False
estou_dando_aula = not estou_desenvolvendo

print(estou_dando_aula)

e_noite_e_estou_desenvolvendo = e_noite and estou_desenvolvendo
e_noite_e_estou_dando_aula = e_noite and estou_dando_aula

# print(e_noite_e_estou_desenvolvendo)
# print(e_noite_e_estou_dando_aula)
